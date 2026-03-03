# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobyn(RPackage):
	"""Semi-Automated Marketing Mix Modeling (MMM) from Meta Marketing
Science

	Semi-Automated Marketing Mix Modeling (MMM) aiming to reduce human bias by means of ridge regression and evolutionary algorithms, enables actionable decision making providing a budget allocation and diminishing returns curves and allows ground-truth calibration to account for causation.
	"""
	
	homepage = "https://github.com/facebookexperimental/Robyn"
	cran = "Robyn" 

	version("3.10.3", md5="b7d295ad2d2933b275a025c8d7d08a6b")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lares", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-prophet", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
