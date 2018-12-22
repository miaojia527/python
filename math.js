const math = require('mathjs')

//四舍五入精度有问题，尾数会出现3分这样的错误
var fixedNumber = function (num, pre=2) {
	if (typeof num !== 'number') num = Number(num)
	if (isNaN(num)) num = 0
	pre += 1
	let precision = Math.pow(10,pre)
	let fixedNum = Number((Math.round(num * precision) / precision).toFixed(pre))
	pre -= 1
	precision = Math.pow(10,pre)
	return Number((Math.round(fixedNum * precision) / precision).toFixed(pre))
}

// toFixed 修复
function toFixed(num, s) {
    var times = Math.pow(10, s)
    var des = num * times + 0.5
    des = parseInt(des, 10) / times
    return des + ''
}
//16位大数，计算错误
console.log(9999999999999999 == 10000000000000001)  //true
