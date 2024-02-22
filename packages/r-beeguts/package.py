# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBeeguts(RPackage):
	"""General Unified Threshold Model of Survival for Bees using
Bayesian Inference

	Tools to calibrate, validate, and make predictions with the
    General Unified Threshold model of Survival adapted for Bee species. The
    model is presented in the publication from Baas, J., Goussen, B., Miles, M.,
    Preuss, T.G., Roessing, I. (2022) <doi:10.1002/etc.5423> and is based on the GUTS framework
    Jager, T., Albert, C., Preuss, T.G. and Ashauer, R. (2011) <doi:10.1021/es103092a>.
    The authors are grateful to Bayer A.G. for its financial support.
	"""
	
	homepage = "https://github.com/bgoussen/BeeGUTS"
	cran = "BeeGUTS" 

	version("1.1.3", md5="6f5f5a6ed47e8380ea4a37847a1a264d")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-rstantools@2.1.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-odeguts", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
