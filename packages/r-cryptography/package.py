# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCryptography(RPackage):
	"""Encrypts and Decrypts Text Ciphers

	Playfair, Four-Square, Scytale, Columnar Transposition and Autokey methods. Further explanation on methods of classical cryptography can be found at Wikipedia; (<https://en.wikipedia.org/wiki/Classical_cipher>).
	"""
	
	homepage = "https://github.com/PiarasFahey/cryptography"
	cran = "cryptography" 

	version("1.0.0", md5="95fb55cb15463a31c41658fda73765dc")

	depends_on("r-desctools", type=("build", "run"))
