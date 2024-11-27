/* eslint-disable */

export default function createInt8TypedArray(length, position, value) {
    if (position >= length || position < 0) {
        throw new Error('Position outside range')
    }

    const view = new DataView(buffer);
    const buffer = new ArrayBuffer(length);

    view.setInt8(postion, value)

    return view;
}
