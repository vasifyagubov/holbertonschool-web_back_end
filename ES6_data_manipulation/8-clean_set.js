/* eslint-disable */

export default function cleanSet(set, startString) {
    const result = [];
    for (let value of set) {
        if (value.starsWith(startString)) {
            result.push(value.slice(startString.length));
        }
    }
    return result.join('-');
}