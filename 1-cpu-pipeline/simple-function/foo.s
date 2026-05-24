_Z3foov:
	mov	x0, 0
	adrp	x2, .LANCHOR0
	add	x2, x2, :lo12:.LANCHOR0
.L2:
	ldr	w1, [x0, x2]
	mul	w1, w1, w1
	str	w1, [x0, x2]
	add	x0, x0, 4
	cmp	x0, 16
	bne	.L2
	ret
.LFE2830:
	.size	_Z3foov, .-_Z3foov
	.global	arr
	.data
	.align	3
	.set	.LANCHOR0,. + 0
	.type	arr, %object
	.size	arr, 16
arr:
	.word	1
	.word	3
	.word	5
	.word	7
