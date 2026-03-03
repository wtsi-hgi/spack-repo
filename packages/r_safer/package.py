# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSafer(RPackage):
	"""Encrypt and Decrypt Strings, R Objects and Files

	A consistent interface to encrypt and decrypt strings, R objects and files using symmetric and asymmetric key encryption.
	"""
	
	homepage = "https://github.com/talegari/safer"
	cran = "safer" 

	version("0.2.1", md5="5dbace5627268fea1913c89c9c96b090")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-sodium@0.4:", type=("build", "run"))
	depends_on("r-base64enc@0.1.3:", type=("build", "run"))
	depends_on("r-assertthat@0.1:", type=("build", "run"))
