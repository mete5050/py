
import tensorflow as tf

x1 = tf.constant(5)
x2 = tf.constant(6)

# Addition, Multiplication and Subtraction
add = tf.add(x1, x2)
#sub = tf.sub(x1, x2)
#mul = tf.mul(x1, x2)

# 1x2 Matrix
matrix1 = tf.constant(
	[
		[3., 4.]
	]
)

# 2x1 Matrix
matrix2 = tf.constant(
	[
		[2.],
		[2.]
	]
)

# Matrix Multiplication
product = tf.matmul(matrix1, matrix2)

# Linearly spaced vector
vector = tf.linspace(-3.0, 7.0, 6)

with tf.Session() as sess:
    print(sess.run(add))
print(sess.run(add))
