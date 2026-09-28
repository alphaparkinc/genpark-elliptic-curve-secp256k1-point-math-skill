from client import Secp256k1Curve

def main():
    priv = 0xDEADBEEF998877
    pub = Secp256k1Curve.scalar_mult(priv)
    print("Computed Secp256k1 Public Key:")
    print("  X:", hex(pub[0]))
    print("  Y:", hex(pub[1]))

if __name__ == "__main__":
    main()
