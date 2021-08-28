require 'json'
require 'uri'
require 'net/http'
require 'http'


def get_info(body,uri_op,type_op)
    port = 5000.to_s
    url = 'http://127.0.0.1:'+port.to_s+uri_op
    
    if type_op == "GET"
        response = HTTP.get(url)
        for index in 0 ... response.parse.size
            student = response.parse[index]
            puts "---------------------------"
            print "\nStudent #{index}\n\n"
            puts "RA: #{student["ra"]}"
            puts "name: #{student["name"]}"
            puts "period: #{student["period"]}"
            puts "course code: #{student["course_code"]}"
            puts "---------------------------"
        end
        
    elsif type_op == "POST"
        uri = URI(url)
        http = Net::HTTP.new(uri.host, uri.port)
        req = Net::HTTP::Post.new(uri.path, 'Content-Type' => 'application/json')
        req.body = body
        res = http.request(req)
        puts "response #{res.body}"
    elsif type_op == "DELETE"
        uri = URI(url)
        http = Net::HTTP.new(uri.host, uri.port)
        req = Net::HTTP::Delete.new(uri.path, 'Content-Type' => 'application/json')
        req.body = body
        res = http.request(req)
        puts "response #{res.body}"
    end
    
rescue => e
    puts "failed #{e}"
end

loopFlag = true
while loopFlag
    puts "1 - Add student grade:"
    puts "2 - Remove student grade:"
    puts "3 - Search students by subject"
    puts "0 - To exit:"
    choose = gets.chomp.to_i
    case choose
    when 1
        puts "Subject Code:"
        subject_code = gets.chomp
        puts "RA:"
        student_ra = gets.chomp.to_i
        puts "Year:"
        year = gets.chomp.to_i
        puts "Semester:"
        semester = gets.chomp.to_i
        puts "Grade:"
        grade = gets.chomp.to_f
        puts "Abscenses:"
        abscenses = gets.chomp.to_i

        body = {
            'subject_code':subject_code,
            'student_ra':student_ra,
            'year':year,
            'semester':semester,
            'grade':grade,
            'abscenses':abscenses
        }.to_json

        get_info(body,'/enrollment','POST')
    when 2
        puts "Subject Code:"
        subject_code = gets.chomp
        puts "RA:"
        student_ra = gets.chomp.to_i
        puts "Year:"
        year = gets.chomp.to_i
        puts "Semester:"
        semester = gets.chomp.to_i
        body = {
            'subject_code':subject_code,
            'student_ra':student_ra,
            'year':year,
            'semester':semester,
        }.to_json
        get_info(body,'/enrollment','DELETE')
    when 3
        puts "Subject code:"
        subject_code = gets.chomp
        
        puts "Year (Optional):"
        year = gets.chomp
        
        puts "Semester (Optional):"
        semester = gets.chomp

        get_info( 
            nil,
            "/students/enrolled?subject_code=" + subject_code + 
            (year.empty? ? "" : "&year=#{year}") + 
            (semester.empty? ? "" : "&semester=#{semester}" ),
            "GET"
        )
    when 0
        puts "Saindo ...."
        loopFlag = false
    end
end