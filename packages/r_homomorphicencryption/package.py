# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHomomorphicencryption(RPackage):
	"""BFV, BGV, CKKS Schema for Fully Homomorphic Encryption

	Implements the Brakerski-Fan-Vercauteren (BFV, 2012) <https://eprint.iacr.org/2012/144>, Brakerski-Gentry-Vaikuntanathan (BGV, 2014) <doi:10.1145/2633600>, and Cheon-Kim-Kim-Song (CKKS, 2016) <https://eprint.iacr.org/2016/421.pdf> schema for Fully Homomorphic Encryption. The included vignettes demonstrate the encryption procedures.
	"""
	
	cran = "HomomorphicEncryption" 

	version("0.9.0", md5="a6ff41c460f827e6e08becadf89cef35")

	depends_on("r-polynom", type=("build", "run"))
	depends_on("r-hetools", type=("build", "run"))
