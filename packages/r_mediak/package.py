# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMediak(RPackage):
	"""Calculate MeDiA_K Distance

	Calculates MeDiA_K (means Mean Distance Association by K-nearest neighbor) in order to detect nonlinear associations. 
	"""
	
	cran = "MediaK" 

	version("1.0", md5="a460b67b343a488f30e6eb21b25d21da")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
