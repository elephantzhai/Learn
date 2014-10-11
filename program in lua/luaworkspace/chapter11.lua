-- 11.1
-- a = {}
-- for i=1,100 do
-- 	a[i] = 0
-- end

-- 11.3
-- list = nil
-- list = {next = list,value = v}

-- local l = list
-- while l do
-- 	print(l.value)
-- 	l = l.next
-- end

-- 11.5
local t = {}
for line in io.lines() do
	table.insert(t,line)
end
s = table.concat( t, "\n") .. "\n"
