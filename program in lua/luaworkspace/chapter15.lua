local function checkCpmplex(c)
	if not ((type(c) == 'table') and tonumber(c.r) and tonumber(c.i)) then
		error("bad complex number","3")
	end	
end

local function new (r,i) return {r=r,i=i} end

local function add (c1,c2)
	checkCpmplex(c1);
	checkCpmplex(c2);
	return new(c1.r + c2.r,c1.i+c2.i);
end

local function tostring(c)
	checkCpmplex(c)
	return "string: "..c.r .." "..c.i
end

complex = {
	new = new,
	add = add,
	tostring = tostring,
}

return complex