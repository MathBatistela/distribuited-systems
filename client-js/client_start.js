const readlineSync = require("readline-sync");
actions = ["Cadastrar Notas","Consultar Notas","Atualizar Notas","Remover Notas", "Consultar Notas e Faltas", "Consultar Alunos de uma disciplina"]
const client = require("./client");


const cadastra_nota = () =>{
    let subject_code = readlineSync.question("Informe o codigo da materia: ");
    let student_ra = readlineSync.question("Informe o RA do aluno: ");
    let year = readlineSync.question("Informe o ano: ");
    let semester = readlineSync.question("Informe o semestre: ");
    let grade = readlineSync.question("Informe a nota: ");
    let abscenses = readlineSync.question("Informe a quantidade de faltas: ");
    return {
        subject_code,
        student_ra,
        year,
        semester,
        grade,
        abscenses}
}

const consulta_notas = () =>{
    let subject_code = readlineSync.question("Informe o codigo da materia: ");
    let student_ra = readlineSync.question("Informe o RA do aluno: ");
    let year = readlineSync.question("Informe o ano: ");
    let semester = readlineSync.question("Informe o semestre: ");
    return {
        subject_code,
        student_ra,
        year,
        semester
    }
}

const atualiza_nota = () =>{
    let subject_code = readlineSync.question("Informe o codigo da materia: ");
    let student_ra = readlineSync.question("Informe o RA do aluno: ");
    let year = readlineSync.question("Informe o ano: ");
    let semester = readlineSync.question("Informe o semestre: ");
    let grade = readlineSync.question("Informe a nota: ");
    let abscenses = readlineSync.question("Informe a quantidade de faltas: ");
    return {
        subject_code,
        student_ra,
        year,
        semester,
        grade,
        abscenses}
}

const remove_nota = () =>{
    let subject_code = readlineSync.question("Informe o codigo da materia: ");
    let student_ra = readlineSync.question("Informe o RA do aluno: ");
    let year = readlineSync.question("Informe o ano: ");
    let semester = readlineSync.question("Informe o semestre: ");
    return{
        subject_code,
        student_ra,
        year,
        semester,
    }
}

const consulta_nota_faltas = () =>{
    let subject_code = readlineSync.question("Informe o codigo da materia: ");
    let year = readlineSync.question("Informe o ano: ");
    let semester = readlineSync.question("Informe o semestre: ");
    return {
        subject_code,
        year,
        semester
    }
}

const consulta_alunos = () =>{
    let subject_code = readlineSync.question("Informe o codigo da materia: ");
    let year = readlineSync.question("Informe o ano: ");
    let semester = readlineSync.question("Informe o semestre: ");
    return {
        subject_code,
        year,
        semester
    }
}


let stopFunc = true;
// while (stopFunc) {
    let index = readlineSync.keyInSelect(actions, 'Qual operação você deseja realizar\n Para sair 0');
    switch (index + 1) {
        case 1:
            console.log(actions[index])
            client.createEnrollment(cadastra_nota(), (error, news) => {
                if (!error) {
                    console.log(news)
                }else{
                    console.error(error)
                }
            });
            break;
        case 2:
            console.log(actions[index])
            client.getEnrollment(consulta_notas(), (error, news) => {
                if (!error) {
                    console.log(news)
                }else{
                    console.error(error)
                }
            });
            break;
        case 3:
            console.log(actions[index])
            client.updateEnrollment(atualiza_nota(), (error, news) => {
                if (!error) {
                    console.log(news)
                }else{
                    console.error(error)
                }
            });
            break;
        case 4:
            console.log(actions[index])
            client.deleteEnrollment(remove_nota(), (error, news) => {
                if (!error) {
                    console.log(news)
                }else{
                    console.error(error)
                }
            });
            break;
        case 5:
            console.log(actions[index])
            client.getAbscensesAndGradesBySubject(consulta_nota_faltas(), (error, news) => {
                if (!error) {
                    console.log(news)
                }else{
                    console.error(error)
                }
            });
            break;
        case 6:
            console.log(actions[index])
            client.getStudentsBySubject(consulta_alunos(), (error, news) => {
                if (!error) {
                    console.log(news)
                }else{
                    console.error(error)
                }
            });
            break;
        case 0:
            stopFunc = false;
            break;
    }
// }