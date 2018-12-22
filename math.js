const math = require('mathjs')

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
