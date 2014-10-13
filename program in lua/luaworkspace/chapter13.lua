-- t = {}
-- print(getmetatable(t))

-- t1 = {}
-- setmetatable(t,t1)
-- print(getmetatable(t) == t1)

-- 13.1
-- Set = {}
-- Set.mt = {}


-- function Set.new(t)
-- 	local  set = {}
-- 	setmetatable(set,Set.mt)
-- 	for _,l in pairs(t) do set[l] = true end
-- 	return set
-- end

-- function Set.union( a,b )
-- 	if getmetatable(a) ~= Set.mt or getmetatable(b) ~= set.mt then
-- 		error("attempt to 'add' a set with a non-set value",2)
-- 	end

-- 	local res = Set.new({})
-- 	for k in pairs(a) do res[k] = true end
-- 	for k in pairs(b) do res[k] = true end
-- 	return res
-- end

-- function Set.intersection( a,b )
-- 	local res = Set.new({})
-- 	for k in pairs(a) do
-- 		res[k] = b[k]
-- 	end
-- 	return res
-- end

-- function Set.tostring(set)
-- 	local s = "{"
-- 	local sep = ""
-- 	for e in pairs(set) do
-- 		s = s .. sep .. e
-- 		sep = ","
-- 	end
-- 	return s .. "}"
-- end

-- function Set.print( s )
-- 	print(Set.tostring(s))
-- end

-- Set.mt.__add = Set.union
-- Set.mt.__mul = Set.intersection


-- s1 = Set.new({10,20,30,50})
-- s2 = Set.new({30,1})
-- s3 = s1+s2
-- Set.print(s3)
-- s4 = s3*s1
-- Set.print(s4)
-- s5 = s4+1

-- 13.2

-- Set = {}
-- Set.mt = {}


-- function Set.new(t)
-- 	local  set = {}
-- 	setmetatable(set,Set.mt)
-- 	for _,l in pairs(t) do set[l] = true end
-- 	return set
-- end

-- Set.mt.__le = function ( a,b )
-- 	for k in pairs(a) do
-- 		if not b[k] then return false end
-- 	end
-- 	return true
-- end

-- Set.mt.__lt = function ( a,b )
-- 	return a<=b and not (b<=a)
-- end

-- Set.mt.__eq = function ( a,b )
-- 	return a<=b and b<=a
-- end

-- s1 = Set.new{2,4}
-- s2 = Set.new{4,10,2}
-- print(s1<=s2)

-- 13.4
-- 13.4.1
-- Window = {}

-- Window.pretotype = {x=0,y=0,width = 100,height=100,}
-- Window.mt = {}

-- function Window.new( o )
-- 	setmetatable(o,Window.mt)
-- 	return o
-- end

-- Window.mt.__index = function ( table,key )
-- 	return Window.pretotype[key]
-- end

-- w = Window.new{x=10,y=20}
-- print(w.width)

-- 13.4.3
-- 有默认值的表
-- local key = {}
-- local mt = {__index = function ( t )
-- 	return t[key]
-- end}

-- function setDefault( t,d )
-- 	t[key] = d
-- 	setmetatable(t,mt)
-- end

-- tab = {x=10,y=20}
-- print(tab.x,tab.z)
-- setDefault(tab,0)
-- print(tab.x,tab.z)

-- 13.4.4
-- 监控表
-- demo1
-- t = {} --original table
-- local _t = t

-- t = {} -- proxy

-- local mt = {
-- 	__index = function ( t,k )
-- 		print ("access to element " .. tostring(k))
-- 		return _t[k]
-- 	end,

-- 	__newindex = function ( t,k,v )
-- 		print("*update of element " .. tostring(k))
-- 		_t[k] = v
-- 	end
-- }
-- setmetatable(t,mt)

-- t[2] = 'hello'
-- print(t[2])

-- demo2
-- local  index = {}
-- local mt = {
-- 	__index = function ( t,k )
-- 		print ("access to element " .. tostring(k))
-- 		return _t[index][k]
-- 	end,

-- 	__newindex = function ( t,k,v )
-- 		print("*update of element " .. tostring(k))
-- 		_t[index][k] = v
-- 	end
-- }
-- function track (t)
-- 	local proxy = {}
-- 	proxy[index] = t
-- 	setmetatable(proxy,mt)
-- 	return proxy
-- end

