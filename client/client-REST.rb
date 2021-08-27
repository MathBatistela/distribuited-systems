require 'json'
require 'uri'
require 'net/http'



def send_info(body,uri_op,type_op)
    port = 5000.to_s
    uri = URI('http://127.0.0.1:'+port.to_s+uri_op)
    if type_op == "GET"
        http = Net::HTTP.new(uri.host, uri.port)
        req = Net::HTTP::Get.new(uri.path, 'Content-Type' => 'application/json')
        req.body = body
        res = http.request(req)
        puts "response #{res.body}"
    elsif type_op == "POST"
        http = Net::HTTP.new(uri.host, uri.port)
        req = Net::HTTP::Post.new(uri.path, 'Content-Type' => 'application/json')
        req.body = body
        res = http.request(req)
        puts "response #{res.body}"
    elsif type_op == "DELETE"
        http = Net::HTTP.new(uri.host, uri.port)
        req = Net::HTTP::Delete.new(uri.path, 'Content-Type' => 'application/json')
        req.body = body
        res = http.request(req)
        puts "response #{res.body}"
    end
    
rescue => e
    puts "failed #{e}"
end

# puts "Informe a porta para conexao"
# student_ra = gets.chomp.to_i


loopFlag = true
while loopFlag
    puts "1 - Adicionar Nota do Aluno:"
    puts "2 - Remover Nota do Aluno:"
    puts "3 - Consultar Aluno"
    puts "0 para sair:"
    choose = gets.chomp.to_i
    case choose
    when 1
        puts "Informe Subject Code"
        subject_code = gets.chomp
        puts "Informe o RA do aluno"
        student_ra = gets.chomp.to_i
        puts "Informe o Ano"
        year = gets.chomp.to_i
        puts "Informe o Semestre"
        semester = gets.chomp.to_i
        # puts "Informe o Grade"
        # grade = gets.chomp.to_f
        # puts "Informe o numero de faltas"
        # abscenses = gets.chomp.to_i
        body = {
            'subject_code':subject_code,
            'student_ra':student_ra,
            'year':year,
            'semester':semester,
        }.to_json
        # 'grade':grade,
        # 'abscenses':abscenses,
        send_info(body,'/enrollment','PUT')
    when 2
        puts "Informe Subject Code"
        subject_code = gets.chomp
        puts "Informe o RA do aluno"
        student_ra = gets.chomp.to_i
        puts "Informe o Ano"
        year = gets.chomp.to_i
        puts "Informe o Semestre"
        semester = gets.chomp.to_i
        puts "Informe o Grade"
        grade = gets.chomp.to_f
        body = {
            'subject_code':subject_code,
            'student_ra':student_ra,
            'year':year,
            'semester':semester,
            'grade':grade
        }.to_json
        send_info(body,'/enrollment','DELETE')
    when 3
        puts "Informe o codigo da materia"
        subject_code = gets.chomp
        
        puts "Opcional: Informe o ano para pesquisar"
        year = gets.chomp.to_i
        
        puts "Opcional:  Informe o semestre"
        semester = gets.chomp.to_i
        body = {'subject_code':subject_code}
        if year != ""
            body['year'] = year
        elsif semester != ""
            body['subject_code'] = subject_code
        end
        
        send_info(body.to_json,"students/enrolled?subject_code="+subject_code,"GETURL")
    when 0
        puts "Saindo ...."
        loopFlag = false
    end
end