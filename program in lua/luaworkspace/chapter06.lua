-- 6.1
network = {
	{name = "grauna",ip = "210.26.30.34"},
	{name = "arraial",ip = "210.26.30.23"},
	{name = "lua",ip="210.26.23.12"},
	{name = "derain", ip = "210.26.23.20"},
}

table.sort(network,function ( a,b )
	return (a.name > b.name)
end)

for i,v in pairs(network) do
	print (v['name'],v['ip'])
end
