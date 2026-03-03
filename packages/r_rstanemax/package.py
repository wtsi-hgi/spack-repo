# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRstanemax(RPackage):
	"""Emax Model Analysis with 'Stan'

	Perform sigmoidal Emax model fit using 'Stan' in a formula notation, without writing 'Stan' model code.
	"""
	
	homepage = "https://github.com/yoshidk6/rstanemax"
	cran = "rstanemax" 

	version("0.1.5", md5="a3ac40643b9c5be1ae3d9126d6d98bcb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp@1:", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-rstantools@2.3:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-dplyr@0.8:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-purrr@0.3:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
	depends_on("r-bh@1.69.0.1:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.5:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.2:", type=("build", "run"))
