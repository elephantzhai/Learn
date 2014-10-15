-- 16.1
-- 类
Account = {balance = 0}

function Account:new( o )
	o  = o or {}
	setmetatable(o,self)
	self.__index = self
	return o
end

function Account:deposit( v )
	self.balance = self.balance +v
end

function Account:withdraw( v )
	if v > self.balance then error "insufficient funds" end
	self.balance = self.balance - v
end

-- b = Account:new()
-- print(b.balance)
-- b:deposit(100)
-- print(b.balance)

-- 16.2
-- 继承
-- SpecialAccount = Account:new()

-- function SpecialAccount:withdraw( v )
-- 	if v - self.balance >= self:getLimit() then
-- 		error "insufficient funds"
-- 	end
-- 	self.balance = self.balance - v
-- end

-- function SpecialAccount:getLimit( )
-- 	return self.limit or 0
-- end

-- s =SpecialAccount:new{limit = 1000.0}
-- s:deposit(100.0)
-- print(s:getLimit(),s.balance)

-- 16.3
-- 多重继承
local function search( k,plist )
	for i = 1,table.getn(plist) do
		local v = plist[i][k]
		if v then return v end
	end
end 

function createClass(...)
	local c = {}

	setmetatable(c,{__index = function ( t,k )
		local v = search(k,arg)
		t[k] = v
		return v
	end})

	c.__index = c

	function c:new( o )
		o = o or {}
		setmetatable(o,c)
		return o
	end

	return c
end


Named = {}
function Named:getname( )
	return self.name
end

function Named:setname( n )
	self.name = n
end

NamedAccount = createClass(Account,Named)
account = NamedAccount:new{name = "Paul"}
print(account.balance)
account:setname("ele")
print(account:getname())


-- 16.4
-- 私有性
function newAccount ( initialBalance )
	local self = {balance = initialBalance}

	local withdraw = function(v)
		self.balance = self.balance - v
	end

	local deposit = function ( v )
		self.balance = self.balance + v
	end

	local getBalence = function ()
		return self.balance
	end

	return{
		withdraw = withdraw,
		deposit = deposit,
		getBalence = getBalence,
	}
end

acc1 = newAccount(100)
acc1.withdraw(40)
print(acc1.getBalence())