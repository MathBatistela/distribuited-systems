require 'socket'
require './pb_files/student_pb.rb'
require './pb_files/server_pb.rb'
require 'objspace'

def wrap(msg,len)
    finalmsg = [msg].pack("v")
    finalLen = [len].pack("V")
    return finalmsg+finalLen
end

def get_data(header,buff)
    server = TCPSocket.open('localhost', 2020)
    server.write buff
    resp = server.read(6)
    method = resp.unpack('v')[0]
    size = resp.unpack('V')[0].to_i
    protobuf = server.read(size)
    return method, protobuf
end

def show_data(method, protobuf)
    if method == 1
        students_response = StudentModule::StudentsResponse.decode(protobuf)
        for index in 0 ... students_response.students.size
            print "Student #{index}\n\n"
            puts "RA: #{students_response.students[index].ra}"
            puts "name: #{students_response.students[index].name}"
            puts "period: #{students_response.students[index].period}"
            puts "course code: #{students_response.students[index].course_code}"
            puts "---------------------------"
        end
    else
        update_response = Server::Response.decode(protobuf)
        print "\n" + update_response.message + "\n\n"
    end
end

loopFlag = true
while loopFlag
    puts "1 - Get students by enrollment:"
    puts "2 - Update Grade:"
    puts "0 to exit:"
    choose = gets.chomp.to_i
    case choose
    when 1
        request = StudentModule::StudentQueryBySubjectRequest.new
        puts "Subject code: "
        request.subject_code = gets.chomp
        puts "Year: "
        request.year = gets.chomp.to_i
        puts "Semester: "
        request.semester = gets.chomp.to_i
        encoded = StudentModule::StudentQueryBySubjectRequest.encode(request)
        header = wrap(1,ObjectSpace.memsize_of(request))
        method, protobuf = get_data(header,encoded)
        show_data(method, protobuf)
    when 2
        request = StudentModule::UpdateGradeRequest.new
        puts "Subject Code"
        request.subject_code = gets.chomp
        puts "Student RA"
        request.student_ra = gets.chomp.to_i
        puts "Year"
        request.year = gets.chomp.to_i
        puts "Semester"
        request.semester = gets.chomp.to_i
        puts "Grade"
        request.grade = gets.chomp.to_i
        encoded = StudentModule::UpdateGradeRequest.encode(request)
        header = wrap(0,ObjectSpace.memsize_of(request))
        method, protobuf = get_data(header,encoded)
        show_data(method, protobuf)
    when 0
        puts "Exiting ...."
        loopFlag = false
    end
end
