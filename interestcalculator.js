const data = [{
        principal: 2500,
        time: 1.8,
    },
    {
        principal: 1000,
        time: 5,
    },
    {
        principal: 3000,
        time: 1,
    },
    {
        principal: 2000,
        time: 3,
    },
];

let rate;

function interestCalculator(array) {
    if (principal >= 2500 && time > 1 && time < 3) {
        return (rate = 3);
    } else if (principal >= 2500 && time >= 3) {
        return (rate = 4);
    } else if (principal < 2500 && time <= 1) {
        return (rate = 2);
    } else {
        return (rate = 1);
    }
}
const interest = (principal * rate * time) / 100;
const interestData = [total.Principal, total.rate, total.Time, total.interest];

console.log(interestCalculator(data));