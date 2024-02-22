# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDymo(RPackage):
	"""Dynamic Mode Decomposition for Multivariate Time Feature
Prediction

	An application of Dynamic Mode Decomposition for prediction of time features. Automatic search for the best model across the space of all possible feature combinations and ranks of Singular Value Decomposition.
	"""
	
	homepage = "https://rpubs.com/giancarlo_vercellino/dymo"
	cran = "dymo" 

	version("1.1.0", md5="7b0834c8e57d2cc968a5b89f44e6a41d")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-readr@2.1.2:", type=("build", "run"))
	depends_on("r-lubridate@1.7.10:", type=("build", "run"))
	depends_on("r-imputets@3.2:", type=("build", "run"))
	depends_on("r-fancova@0.6.1:", type=("build", "run"))
	depends_on("r-scales@1.1.1:", type=("build", "run"))
	depends_on("r-tictoc@1.0.1:", type=("build", "run"))
	depends_on("r-modeest@2.4:", type=("build", "run"))
	depends_on("r-moments@0.14:", type=("build", "run"))
	depends_on("r-greybox@1.0.1:", type=("build", "run"))
	depends_on("r-mass@7.3.54:", type=("build", "run"))
	depends_on("r-matlib@0.9.5:", type=("build", "run"))
	depends_on("r-narray@0.4.1.1:", type=("build", "run"))
