#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np

def conv2d(image, kernel):
    image_height, image_width = image.shape
    kernel_height, kernel_width = kernel.shape
    
    output_height = image_height - kernel_height + 1
    output_width = image_width - kernel_width + 1
    output = np.zeros((output_height, output_width))
    
    for i in range(output_height):
        for j in range(output_width):
            output[i, j] = np.sum(image[i:i+kernel_height, j:j+kernel_width] * kernel)
    
    return output

x_rows = int(input("Enter the number of rows for the input matrix x: "))
x_cols = int(input("Enter the number of columns for the input matrix x: "))

print("Enter the values for the input matrix x (row-wise):")
x = np.zeros((x_rows, x_cols))
for i in range(x_rows):
    x[i] = list(map(float, input().split()))

h_rows = int(input("Enter the number of rows for the kernel h: "))
h_cols = int(input("Enter the number of columns for the kernel h: "))

print("Enter the values for the kernel h (row-wise):")
h = np.zeros((h_rows, h_cols))
for i in range(h_rows):
    h[i] = list(map(float, input().split()))

result = conv2d(x, h)

print("Input Image (x):")
print(x)
print("\nKernel (h):")
print(h)
print("\nConvolution Result:")
print(result)


# In[ ]:




