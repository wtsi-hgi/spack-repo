# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RThurstonianirt(RPackage):
	"""Thurstonian IRT Models

	Fit Thurstonian Item Response Theory (IRT) models in R. This 
  package supports fitting Thurstonian IRT models and its extensions using 
  'Stan', 'lavaan', or 'Mplus' for the model estimation. Functionality for 
  extracting results, making predictions, and simulating data is provided as 
  well. References: 
  Brown & Maydeu-Olivares (2011) <doi:10.1177/0013164410375112>;
  Bürkner et al. (2019) <doi:10.1177/0013164419832063>.
	"""
	
	homepage = "https://github.com/paul-buerkner/thurstonianIRT"
	cran = "thurstonianIRT" 

	version("0.12.4", md5="5dffdfd597f1d5172cbbf4cc2aa55ce8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp@0.12.16:", type=("build", "run"))
	depends_on("r-dplyr@0.6:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-rstantools@2.1.1:", type=("build", "run"))
	depends_on("r-tibble@1.3.1:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-lavaan@0.6.1:", type=("build", "run"))
	depends_on("r-bh@1.66.0.1:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.4:", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
