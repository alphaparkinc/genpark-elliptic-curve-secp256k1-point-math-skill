"""Secp256k1 Elliptic Curve Group Operations.
100% Python Standard Library.
"""

class Secp256k1Curve:
    """Weierstrass elliptic curve y^2 = x^3 + 7 (mod P) point arithmetic."""
    P = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
    A = 0
    B = 7
    Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
    Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
    N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

    @classmethod
    def point_add(cls, p1, p2):
        if p1 is None:
            return p2
        if p2 is None:
            return p1
        x1, y1 = p1
        x2, y2 = p2
        if x1 == x2 and y1 != y2:
            return None
        if x1 == x2 and y1 == y2:
            m = (3 * x1 * x1 + cls.A) * pow(2 * y1, cls.P - 2, cls.P) % cls.P
        else:
            m = (y2 - y1) * pow(x2 - x1, cls.P - 2, cls.P) % cls.P
        x3 = (m * m - x1 - x2) % cls.P
        y3 = (m * (x1 - x3) - y1) % cls.P
        return (x3, y3)

    @classmethod
    def scalar_mult(cls, k: int, point=None):
        if point is None:
            point = (cls.Gx, cls.Gy)
        result = None
        addend = point
        while k:
            if k & 1:
                result = cls.point_add(result, addend)
            addend = cls.point_add(addend, addend)
            k >>= 1
        return result
