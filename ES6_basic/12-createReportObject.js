/* eslint-disable */
export default function createReportObject(employeesList) {
    return {
        allEmployees: {
            ...employeesList
        },
        getNumberOfDepartments(){
            return Objects.keys(employeesList).length;
        },
      };
}