# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSecure(RPackage):
	"""Sequential Co-Sparse Factor Regression

	Sequential factor extraction via co-sparse unit-rank estimation (SeCURE).
	"""
	
	cran = "secure" 

	version("0.6", md5="04f7a4743d9fc22efa4edc7e49770f2e")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
