function getRandomValue()	
    print('Caling Random')
	math.randomseed(os.time())
	x = math.random()
	x = math.floor(x * 10) 
	x = x + 1
	return(x)
end

print('Priming Run')
