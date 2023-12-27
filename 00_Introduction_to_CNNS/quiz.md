# Images in Data Visualization
```py
# Set the red channel in this part of the image to 1
data[:10, :10, 0] = 1
# print(data.shape)
# Set the green channel in this part of the image to 0
data[:10, :10, 1] = 0

# Set the blue channel in this part of the image to 0
data[:10, :10, 2] = 0

# Visualize the result
plt.imshow(data)
print(data)
plt.show()
```