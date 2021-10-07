import tensorflow as tf

@tf.function
def get_entropy(x: tf.Tensor, y: tf.Tensor, epsilon = 1e-7)->float:
    """
    Kullbac Liebler Divergence
    """
    #entropy(x.numpy(), y.numpy(), base=np.exp(1))
    #tf.reduce_sum(x*tf.math.log(x/y),0)
    
    x = tf.clip_by_value(x, tf.constant(epsilon, dtype=x.dtype), tf.constant(1, dtype=x.dtype))
    y = tf.clip_by_value(y, tf.constant(epsilon, dtype=y.dtype), tf.constant(1, dtype=y.dtype))
    
    return tf.keras.losses.KLD(x,y)

@tf.function
def get_array_entropy(first: tf.Tensor, second: tf.Tensor):
    return tf.map_fn(lambda xi: 
              tf.map_fn(lambda yi: get_entropy(xi,yi), second),
          first, parallel_iterations=12)