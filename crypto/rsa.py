"""
    Educational RSA implementation.

    This module implements the RSA cryptosystem for didactic purposes only.
    Real-world RSA uses primes of 2048+ bits and additional safeguards
    (padding, secure random, etc.) that this implementation does NOT include.
"""


def gcd(a, b):
    """
        Greatest common divisor (Euclidean algorithm).
        Complexity: O(log(min(a, b))).
    """
    while b:
        a, b = b, a % b
    return a


def extended_gcd(a, b):
    """
        Extended Euclidean algorithm.
        Returns (g, x, y) such that a*x + b*y = g = gcd(a, b).
        Complexity: O(log(min(a, b))).
    """
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y


def mod_inverse(e, phi):
    """
        Modular inverse of e modulo phi: returns d such that (d*e) % phi == 1.
        Uses extended Euclidean algorithm.
        Complexity: O(log(phi)).
    """
    g, x, _ = extended_gcd(e, phi)
    if g != 1:
        raise ValueError(f"e={e} and phi={phi} are not coprime; no modular inverse exists.")
    return x % phi


class RSA:
    """
        Educational RSA cryptosystem.

        Given two primes p and q, computes the public/private key pair
        and exposes encrypt/decrypt for short messages.

        Security note: this is a TOY implementation. It does NOT use
        secure padding (OAEP), does NOT validate primes are large enough,
        and is not suitable for any real cryptographic use.
    """

    def __init__(self, p, q, e=65537):
        """
            Build the RSA key pair from two primes p and q.
            e is the public exponent (default 65537, the standard choice).
        """
        if p == q:
            raise ValueError("p and q must be distinct primes.")
        self.p = p
        self.q = q
        self.n = p * q
        self.phi = (p - 1) * (q - 1)
        # If e is too large for these small primes, fall back to a small coprime.
        if e >= self.phi or gcd(e, self.phi) != 1:
            e = self._pick_public_exponent()
        self.e = e
        self.d = mod_inverse(self.e, self.phi)

    def _pick_public_exponent(self):
        """Find a small e coprime with phi. Used when 65537 doesn't fit."""
        for candidate in (3, 5, 7, 11, 13, 17, 19, 23):
            if candidate < self.phi and gcd(candidate, self.phi) == 1:
                return candidate
        raise ValueError("No small public exponent coprime with phi found.")

    def public_key(self):
        """Return (n, e). O(1)."""
        return (self.n, self.e)

    def private_key(self):
        """Return (n, d). O(1)."""
        return (self.n, self.d)

    def encrypt(self, message):
        """
            Encrypt a message. If `message` is a string, encrypt char by char.
            If it's an int, encrypt directly.
            Returns a list of ciphertext integers (or a single int).
            Complexity: O(L * log(e) * log(n)^2) for a string of length L.
        """
        if isinstance(message, str):
            return [pow(ord(ch), self.e, self.n) for ch in message]
        elif isinstance(message, int):
            if message >= self.n:
                raise ValueError(f"Message {message} >= n={self.n}; cannot encrypt.")
            return pow(message, self.e, self.n)
        else:
            raise TypeError("message must be str or int.")

    def decrypt(self, ciphertext):
        """
            Decrypt a ciphertext produced by encrypt().
            If `ciphertext` is a list, decrypt char by char back to a string.
            If it's an int, decrypt to an int.
            Complexity: O(L * log(d) * log(n)^2) for a list of length L.
        """
        if isinstance(ciphertext, list):
            return ''.join(chr(pow(c, self.d, self.n)) for c in ciphertext)
        elif isinstance(ciphertext, int):
            return pow(ciphertext, self.d, self.n)
        else:
            raise TypeError("ciphertext must be list or int.")
