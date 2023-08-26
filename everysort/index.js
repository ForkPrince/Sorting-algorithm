function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}

function sort(arr) {
    const permsList = permute(arr);
    const iterations = permsList.length;

    for (let idx = 0; idx < iterations; idx++) {
        const perm = permsList[idx];
        let sortedFlag = true;

        for (let i = 0; i < perm.length - 1; i++) {
            if (perm[i] > perm[i + 1]) {
                sortedFlag = false;
                break;
            }
        }

        if (sortedFlag) return perm;

        console.log(`Iteration ${idx + 1}/${iterations}: [${perm}]`);
    }
}

function permute(arr) {
    const result = [];

    function permuteHelper(arr, current = []) {
        if (arr.length === 0) result.push([...current]);
        else {
            for (let i = 0; i < arr.length; i++) {
                const remaining = arr.slice(0, i).concat(arr.slice(i + 1));
                current.push(arr[i]);
                permuteHelper(remaining, current);
                current.pop();
            }
        }
    }

    permuteHelper(arr);
    return result;
}

const unsortedArray = Array.from({ length: 10 }, (_, i) => i);
shuffleArray(unsortedArray);

const startTime = new Date().getTime();
const sortedArray = sort(unsortedArray);
const endTime = new Date().getTime();

const elapsedSeconds = (endTime - startTime) / 1000;

console.log("Unsorted array:", unsortedArray);
console.log("Sorted array:", sortedArray);
console.log(`Sorted in ${elapsedSeconds.toFixed(6)} seconds`);
