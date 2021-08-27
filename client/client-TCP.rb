require 'socket'
require '../protocol_buffers/student.pb'
require 'objspace'
def wrap(msg,len)
    finalmsg = [msg].pack("v")
    finalLen = [len].pack("V")
    return finalmsg+finalLen
end

def send_info(header,buff)
    server = TCPSocket.open('localhost', 2020) # conecta ao servidor na porta 3001
    server.write header
    server.write buff
    resp = server.recvfrom( 10000 ) # recebe a mensagem -10000 bytes - do servidor
    p resp
    server.close
end


loopFlag = true
while loopFlag
    puts "1 - Adicionar/Remover Notas do Aluno:"
    puts "2 - Update Grade:"
    puts "0 para sair:"
    choose = gets.chomp.to_i
    case choose
    when 1
        student = Student.new
        puts "Informe o RA do aluno"
        student.ra = gets.chomp.to_i
        puts "Informe o Nome do aluno"
        student.name = gets.chomp
        puts "Informe o periodo do Aluno"
        student.period = gets.chomp.to_i
        puts "Informe o Codigo da disciplina"
        student.course_code = gets.chomp.to_i
        header = wrap(1,ObjectSpace.memsize_of(student))
        send_info(header,student)
    when 2
        gradeUpdate = UpdateGradeRequest.new
        puts "Informe Subject Code"
        gradeUpdate.subject_code = gets.chomp
        puts "Informe o RA do aluno"
        gradeUpdate.student_ra = gets.chomp.to_i
        puts "Informe o Ano"
        gradeUpdate.year = gets.chomp.to_i
        puts "Informe o Semestre"
        gradeUpdate.semester = gets.chomp.to_i
        puts "Informe o Grade"
        gradeUpdate.grade = gets.chomp.to_f
        header = wrap(0,ObjectSpace.memsize_of(gradeUpdate))
        send_info(header,gradeUpdate)
    when 0
        puts "Saindo ...."
        loopFlag = false
    end
end
