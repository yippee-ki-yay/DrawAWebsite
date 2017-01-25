import tensorflow as tf
import scipy.ndimage
import numpy as np

sess = tf.Session()

new_saver = tf.train.import_meta_graph("./models/model.ckpt.meta")

restore = new_saver.restore(sess, './models/model.ckpt')

print new_saver

data = np.vectorize(lambda x: 255 - x)(np.ndarray.flatten(scipy.ndimage.imread("./test_images/8.jpg", flatten=True)))
result = sess.run(tf.argmax(y, 1), feed_dict={x: [data]})

print result
