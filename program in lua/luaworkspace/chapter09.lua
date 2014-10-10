-- 9-1
-- co = coroutine.create(function ()
-- 		print("hi")
-- 	end)
-- print(coroutine.status(co))
-- coroutine.resume(co)
-- print(coroutine.status(co))

-- co = coroutine.create(function ()
-- 	for i=1,10 do
-- 		print ("co",i)
-- 		coroutine.yield()
-- 	end
-- end)
-- for i = 1,10 do
-- 	coroutine.resume(co)
-- end

-- co = coroutine.create(function ( a,b,c)
-- 	print('co',a,b,c)
-- end)
-- coroutine.resume(co,1,2,3)

-- co = coroutine.create(function (a,b)
-- 	coroutine.yield(a+b,a-b)
-- end)
-- print(coroutine.resume(co,10,20))

-- co = coroutine.create(function ()
-- 	print("co",coroutine.yield()	
-- end)
-- coroutine.resume(co)
-- coroutine.resume(co,4,5)

-- co = coroutine.create(function ( )
-- 	return 6,7
-- end)
-- print(coroutine.resume(co))


-- 9-2
-- function receive(prod)
-- 	local  status,value = coroutine.resume(prod)
-- 	return value
-- end

-- function send(x)
-- 	coroutine.yield(x)
-- end

-- function producer()
-- 	return coroutine.create(function ()
-- 		while true do
-- 			local x = io.read()
-- 			send(x)
-- 		end
-- 	end)
-- end

-- function filter(prod )
-- 	return coroutine.create(function ()
-- 		local line = 1
-- 		while true do
-- 			local x = receive(prod)
-- 			x = string.format("%5d %s",line,x)
-- 			send(x)
-- 			line = line+1
-- 		end
-- 	end)
-- end

-- function  consumer(prod)
-- 	while true do
-- 		local x = receive(prod)
-- 		io.write(x,"\n")
-- 	end
-- end

-- p = producer()
-- f = filter(p)
-- consumer(f)

-- 9-3

-- function permgen(a,n)
-- 	if n ==0 then
-- 		printResult(a)
-- 	else
-- 		for i = 1,n do
-- 			a[n],a[i] = a[i],a[n]

-- 			permgen(a,n-1)

-- 			a[n],a[i] = a[i],a[n]
-- 		end
-- 	end
-- end

-- function printResult(a)
-- 	for i,v in pairs(a) do
-- 		io.write(v," ")
-- 	end
-- 	io.write("\n")
-- end

-- permgen({1,2,3,4},4)

-- function permgen(a,n)
-- 	if n ==0 then
-- 		coroutine.yield(a)
-- 	else
-- 		for i = 1,n do
-- 			a[n],a[i] = a[i],a[n]

-- 			permgen(a,n-1)

-- 			a[n],a[i] = a[i],a[n]
-- 		end
-- 	end
-- end

-- function perm(a)
-- 	local  n = table.getn(a)
-- 	local  co = coroutine.create(function ( )
-- 		permgen(a,n)
-- 	end)
-- 	return function ()
-- 		local code,res = coroutine.resume(co)
-- 		return res
-- 	end
-- end

-- function printResult(a)
-- 	for i,v in pairs(a) do
-- 		io.write(v," ")
-- 	end
-- 	io.write("\n")
-- end

-- for p in perm({'a','b','c'}) do
-- 	printResult(p)
-- end

-- 9-4
local socket = require("socket")
print (socket._VERSION)
local host = "www.baidu.com"
local file = "/"
 
-- 创建一个 TCP 连接，连接到 HTTP 连接的标准端口 -- 80 端口上
local sock = assert(socket.connect(host, 80))
sock:send("GET " .. file .. " HTTP/1.0\r\n\r\n")
repeat
    -- 以 1K 的字节块来接收数据，并把接收到字节块输出来
    local chunk, status, partial = sock:receive(1024)
    print(chunk or partial)
until status ~= "closed"
-- 关闭 TCP 连接
sock:close()

-- local http = require("socket.http")
-- local response = http.request("http://www.baidu.com/")
-- print(response)