# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRwfec(RPackage):
	"""R Wireless, Forward Error Correction

	Communications simulation package supporting forward error correction.
	"""
	
	cran = "rwfec" 

	version("0.2", md5="bf1d7d7ffa4660a357d1793190d6d181")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
