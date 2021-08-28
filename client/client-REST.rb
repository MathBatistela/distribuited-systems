"""
Rest client that comunicates with HTTP server over REST using JSON
manage student grades + enrollment
Authors:
    @MathBatistela
    @mvgolom

Created at: 22/08/2021
Updated at: 23/08/2021
Updated at: 27/08/2021
"""

require 'json'
require 'uri'
require 'net/http'
require 'http'

# function send and receive server informations
def get_info(body,uri_op,type_op)
    port = 5000.to_s
    url = 'http://127.0.0.1:'+port.to_s+uri_op
    # realize get operations
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
    # Post operations
    elsif type_op == "POST"
        uri = URI(url)
        http = Net::HTTP.new(uri.host, uri.port)
        req = Net::HTTP::Post.new(uri.path, 'Content-Type' => 'application/json')
        req.body = body
        res = http.request(req)
        puts "response #{res.body}"
    # Delete Operations
    elsif type_op == "DELETE"
        uri = URI(url)
        http = Net::HTTP.new(uri.host, uri.port)
        req = Net::HTTP::Delete.new(uri.path, 'Content-Type' => 'application/json')
        req.body = body
        res = http.request(req)
        puts "response #{res.body}"
    end
# handle error http
rescue => e
    puts "failed #{e}"
end

loopFlag = true
# main loop 
while loopFlag
    puts "1 - Add student grade:"
    puts "2 - Remove student grade:"
    puts "3 - Search students by subject"
    puts "0 - To exit:"
    choose = gets.chomp.to_i
    case choose
# create grade
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
        # body of message
        body = {
            'subject_code':subject_code,
            'student_ra':student_ra,
            'year':year,
            'semester':semester,
            'grade':grade,
            'abscenses':abscenses
        }.to_json
        # body of message, URL, Type of Requisition
        get_info(body,'/enrollment','POST')
# delete grade
    when 2
        puts "Subject Code:"
        subject_code = gets.chomp
        puts "RA:"
        student_ra = gets.chomp.to_i
        puts "Year:"
        year = gets.chomp.to_i
        puts "Semester:"
        semester = gets.chomp.to_i
        # body of message
        body = {
            'subject_code':subject_code,
            'student_ra':student_ra,
            'year':year,
            'semester':semester,
        }.to_json
        get_info(body,'/enrollment','DELETE')
# search student by enrolled
    when 3
        puts "Subject code:"
        subject_code = gets.chomp
        
        puts "Year (Optional):"
        year = gets.chomp
        
        puts "Semester (Optional):"
        semester = gets.chomp
        # body of message and URL
        get_info( 
            nil,
            "/students/enrolled?subject_code=" + subject_code + 
            (year.empty? ? "" : "&year=#{year}") + 
            (semester.empty? ? "" : "&semester=#{semester}" ),
            "GET"
        )
# exit main loop
    when 0
        puts "Saindo ...."
        loopFlag = false
    end
end