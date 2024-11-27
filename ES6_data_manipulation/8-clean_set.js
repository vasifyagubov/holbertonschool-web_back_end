/* eslint-disable */

export default function cleanSet(set, startString) {
    const result = [];
    for (let value of set) {
        if (value.slice(0, startString.length) === startString) {
            result.push(value.slice(startString.length));
        }
    }
    return result.join('-');
}