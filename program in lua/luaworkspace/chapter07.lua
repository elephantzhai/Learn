-- 7.1
-- function list_iter(t)
-- 	local i = 0
-- 	local n = table.getn(t)
-- 	return function ()
-- 		i = i + 1
-- 		if i <= n then return t[i] end
-- 	end
-- end

-- t = {10,20,30}
-- iter = list_iter(t)
-- while true do
-- 	local element = iter()
-- 	if element == nil then break end
-- 	print (element)
-- end

-- for element in list_iter(t) do
-- 	print(element)
-- end


-- function allwords()
-- 	local line = io.read()
-- 	local pos = 1
-- 	return function ()
-- 		while line do
-- 			local s,e = string.find(line,"%w+",pos)
-- 			if s then
-- 				pos = e+1
-- 				return string.sub(line,s,e)
-- 			else
-- 				line = io.read()
-- 				pos = 1
-- 			end
-- 		end
-- 		return nil
-- 	end
-- end

-- for word in allwords() do
-- 	print(word)
-- end

-- 7.4
-- local iterator

-- function allwords()
-- 	local state = {line = io.read(),pos=1}
-- 	return iterator,state
-- end

-- function iterator(state)
-- 	while state.line do
-- 		local s,e = string.find(state.line,"%w+",state.pos)
-- 		if s then
-- 			state.pos = e + 1
-- 			return string.sub(state.line,s,e)
-- 		else
-- 			state.line = io.read()
-- 			state.pos = 1
-- 		end
-- 	end
-- 	return nil
-- end

-- 7.5
function allwords(f)
	for l in io.lines() do
		for w in string.gfind(l,"%w+") do
			f(w)
		end
	end
end
allwords(print)




