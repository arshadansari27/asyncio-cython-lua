#include <lua.h>
#include <lauxlib.h>

/* Convenience stuff */
static void close_state(lua_State **L) { lua_close(*L); }
#define cleanup(x) __attribute__((cleanup(x)))
#define auto_lclose cleanup(close_state) 

static int on_recv(lua_State *L, char *buf, size_t len)
{
    lua_getglobal(L, "getRandomValue");
    lua_pushlstring(L, buf, len); /* Binary strings are okay */
    int ret = lua_pcall(L, 1, 1, 0); /* 1 argument, 1 result */
    printf("ret: %d, buflen: %ld\n", ret, lua_tointeger(L, -1));
    lua_pop(L, 1);
    return ret;
}

int myfunc()
{
    /* Create VM state */
    auto_lclose lua_State *L = luaL_newstate();
    if (!L)
        return 1;
    luaL_openlibs(L); /* Open standard libraries */
    /* Load config file */
    luaL_loadfile(L, "lua_code.lua"); /* (1) */
    int ret = lua_pcall(L, 0, 0, 0);
    if (ret != 0) {
        fprintf(stderr, "%s\n", lua_tostring(L, -1));
        return 1;
    }
    /* Read out config */
    lua_getglobal(L, "address"); /* (2) */
    lua_getglobal(L, "port");
    printf("address: %s, port: %ld\n", /* (3) */
        lua_tostring(L, -2), lua_tointeger(L, -1));
    lua_settop(L, 0); /* (4) */
	char buf[512] = { 0x05, 'h', 'e', 'l', 'l', 'o' };
    on_recv(L, buf, sizeof(buf));
    return 1;
}
