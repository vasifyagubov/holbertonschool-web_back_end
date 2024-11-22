/* eslint-disable */

export default function getStudentsByLocataion(students, city) {
    return students.filter(a => a.location === city);
}