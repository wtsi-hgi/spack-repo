# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSodium(RPackage):
	"""A Modern and Easy-to-Use Crypto Library

	Bindings to 'libsodium' <https://doc.libsodium.org/>: a modern, 
    easy-to-use software library for encryption, decryption, signatures, password
    hashing and more. Sodium uses curve25519, a state-of-the-art Diffie-Hellman 
    function by Daniel Bernstein, which has become very popular after it was 
    discovered that the NSA had backdoored Dual EC DRBG.
	"""
	
	homepage = "https://docs.ropensci.org/sodium/"
	cran = "sodium" 

	version("1.3.1", md5="05f45dd77035afe37af4b2726d048453")

	depends_on("libsodium@1.0.3:", type=("build", "link", "run"))
