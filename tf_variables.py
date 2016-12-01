import tensorflow as tf 

if __name__ == '__main__':
	new_value = tf.Variable(0 , name="count")
	new_value = tf.assign ( new_value, tf.add(new_value , tf.constant(1)))
	with tf.Session() as sess:
		sess.run(tf.initialize_all_variables())
		for _ in range(3):
			print(sess.run(new_value))
