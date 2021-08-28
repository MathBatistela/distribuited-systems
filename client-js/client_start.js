/*
Grpc client that comunicates with Protobuff server over Protobuff
manage student + grades + enrollment
Authors:
    @MathBatistela
    @mvgolom

Created at: 22/08/2021
Updated at: 23/08/2021
Updated at: 27/08/2021
*/
const readlineSync = require("readline-sync");
// cli options
actions = ["Cadastrar Notas","Consultar Notas","Atualizar Notas","Remover Notas", "Consultar Notas e Faltas", "Consultar Alunos de uma disciplina"]
// load client config file
const client = require("./client");

// functions create grade
const create_grade = () =>{
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
// functions search grade by RA
const search_grade = () =>{
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
// functions update grade
const update_grade = () =>{
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
// functions update grade
const remove_grade = () =>{
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
// functions search grade and abscenses
const search_grade_abscenses = () =>{
    let subject_code = readlineSync.question("Informe o codigo da materia: ");
    let year = readlineSync.question("Informe o ano: ");
    let semester = readlineSync.question("Informe o semestre: ");
    return {
        subject_code,
        year,
        semester
    }
}
// functions search student by RA
const search_student = () =>{
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
        //create grade
        case 1:
            console.log(actions[index])
            client.createEnrollment(create_grade(), (error, news) => {
                if (!error) {
                    console.log(news)
                }else{
                    console.error(error)
                }
            });
            break;
        //search grade
        case 2:
            console.log(actions[index])
            client.getEnrollment(search_grade(), (error, news) => {
                if (!error) {
                    console.log(news)
                }else{
                    console.error(error)
                }
            });
            break;
        //update grade
        case 3:
            console.log(actions[index])
            client.updateEnrollment(update_grade(), (error, news) => {
                if (!error) {
                    console.log(news)
                }else{
                    console.error(error)
                }
            });
            break;
        //remove grade
        case 4:
            console.log(actions[index])
            client.deleteEnrollment(remove_grade(), (error, news) => {
                if (!error) {
                    console.log(news)
                }else{
                    console.error(error)
                }
            });
            break;
        //search grade abscenses
        case 5:
            console.log(actions[index])
            client.getAbscensesAndGradesBySubject(search_grade_abscenses(), (error, news) => {
                if (!error) {
                    console.log(news)
                }else{
                    console.error(error)
                }
            });
            break;
        //search student by RA
        case 6:
            console.log(actions[index])
            client.getStudentsBySubject(search_student(), (error, news) => {
                if (!error) {
                    console.log(news)
                }else{
                    console.error(error)
                }
            });
            break;
        //exit
        case 0:
            stopFunc = false;
            break;
    }
// }