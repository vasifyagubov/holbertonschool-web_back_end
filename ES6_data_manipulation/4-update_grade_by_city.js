/* eslint-disable */

export default function updateStudentGradeByCity() {
    return students 
    .filter(student => student.location === city)
    .map(student => {
        const studentGrade = newGrade.find(grade => grade.studentId = student.id);
        return {
            ...student,
            grade: studentGrade ? studentGrade.grade: 'N/A'
        };

    }

    )
}
