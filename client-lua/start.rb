require 'socket'
require '../protocol_buffers/student.pb'

def wrap(msg,len)
    finalmsg = [msg].pack("v")
    finalLen = [len].pack("V")
    return finalmsg+finalLen
end


# server = TCPSocket.open('localhost', 2020) # conecta ao servidor na porta 3001
# server.write wrap(1,150)
# resp = server.recvfrom( 10000 ) # recebe a mensagem -10000 bytes - do servidor
# puts resp

# server.close

# loopFlag = true
# while loopFlag
#     puts "1 - Adicionar Aluno:"
#     puts "2 - Update Grade:"
#     puts "0 para sair:"
#     choose = gets.chomp.to_i
#     case choose
#     when 1
      
#     when 2
#         puts "It's 6"
#     else
#       "You gave me #{choose} -- I have no idea what to do with that."
#     end
    
#     if choose == 0
#         puts "Saindo ...."
#         loopFlag = false
#     end
# end

#let student = { ra: 156893, name: 'test', age: 2, period: 5, course_code: 42225 };

user = Student.new
user.ra = 156893
user.name = "Christmas"
user.period = 5
user.course_code = 42225

p user