# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpenssl(RPackage):
	"""Toolkit for Encryption, Signatures and Certificates Based on OpenSSL.

	Bindings to OpenSSL libssl and libcrypto, plus custom SSH pubkey parsers.
	Supports RSA, DSA and EC curves P-256, P-384 and P-521.  Cryptographic
	signatures can either be created and verified manually or via x509
	certificates. AES can be used in cbc, ctr or gcm mode for symmetric
	encryption; RSA for asymmetric (public key) encryption or EC for Diffie
	Hellman. High-level envelope functions combine RSA and AES for encrypting
	arbitrary sized data. Other utilities include key generators, hash
	functions (md5, sha1, sha256, etc), base64 encoder, a secure random number
	generator, and 'bignum' math methods for manually performing crypto
	calculations on large multibyte integers."""

	cran = "openssl"

	version("2.1.1", md5="638ba0b9ff6d9376e21a9063ce4dd20a")

	depends_on("r-askpass", type=("build", "run"))
	depends_on("openssl@1.0.2:", type=("build", "link", "run"))

	def flag_handler(self, name, flags):
		if name == "cflags":
			flags.append(self.compiler.c99_flag)
		return (flags, None, None)
