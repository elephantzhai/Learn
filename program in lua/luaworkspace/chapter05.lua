-- 5.1
f = string.find
a = {"hello","ll"}
print(f(unpack(a)))
print(string.find("hello"))

-- 5.2
function printargs( ... )
	for i,v in pairs(arg) do
		print(i,v)
end

