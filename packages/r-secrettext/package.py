# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSecrettext(RPackage):
	"""Encrypt Text Using a Shifting Substitution Cipher

	Encrypt text using a simple shifting substitution cipher with setcode(), providing two numeric keys used to define the encryption algorithm. The resulting text can be decoded using decode() function and the two numeric keys specified during encryption.
	"""
	
	cran = "secrettext" 

	version("0.1.0", md5="7241b9723470596de32e6954e6003689")

	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
