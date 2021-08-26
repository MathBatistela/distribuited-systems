local host, port = "127.0.0.1", 2020
local socket = require("socket")
local hex = require("hex")
local tcp = assert(socket.tcp())

tcp:connect(host, port);
--note the newline below
tcp:send(string.tohex(25));

while true do
    local s, status, partial = tcp:receive()
    print(s or partial)
    if status == "closed" then break end
end
tcp:close()