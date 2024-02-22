# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSaens(RPackage):
	"""Small Area Estimation with Cluster Information for Estimation of
Non-Sampled Areas

	Implementation of small area estimation (Fay-Herriot model) with EBLUP (Empirical Best Linear Unbiased Prediction) Approach for non-sampled area estimation by adding cluster information and assuming that there are similarities among particular areas. See also Rao & Molina (2015, ISBN:978-1-118-73578-7) and Anisa et al. (2013) <doi:10.9790/5728-10121519>.
	"""
	
	homepage = "https://github.com/Alfrzlp/sae-ns"
	cran = "saens" 

	version("0.1.0", md5="24e36da30041313ae60a1264528f35bc")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
