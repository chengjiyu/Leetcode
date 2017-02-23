# Find the total area covered by two rectilinear rectangles in a 2D plane.
# Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.
# Assume that the total area is never beyond the maximum possible value of int.
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        # 判断是否重叠
        if B >= H or E >= C or F >= D or A >= G:
            return (C-A)*(D-B)+(G-E)*(H-F)
        width = min(C, G) - max(A, E)
        height = min(D, H) - max(B, F)
        return (C-A)*(D-B)+(G-E)*(H-F) - width*height
        # 计算重叠面积，不重叠时面积为0
        width = max(0, min(C, G)-max(A, E))
        height = max(0, min(D, H)-max(B, F))
        return (C-A)*(D-B)+(G-E)*(H-F) - width*height
        # 直接求重叠举行的左下，右下坐标
        left = max(A, E)
        right = max(min(C,G), left)
        bottom = max(B, F)
        top = max(min(D, H), bottom)
        return (C-A)*(D-B)+(G-E)*(H-F) - (right-left)*(top-bottom)
