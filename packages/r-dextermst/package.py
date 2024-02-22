# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDextermst(RPackage):
	"""CML and Bayesian Calibration of Multistage Tests

	Conditional Maximum Likelihood Calibration and data management of multistage tests. 
  Supports polytomous items and incomplete designs with linear as well as multistage tests.
  Extended Nominal Response and Interaction models, DIF and profile analysis.
  See Robert J. Zwitser and Gunter Maris (2015)<doi:10.1007/s11336-013-9369-6>.
	"""
	
	homepage = "https://dexter-psychometrics.github.io/dexter/"
	cran = "dexterMST" 

	version("0.9.6", md5="a5898343dc4c1e50eae5175312049d59")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.12.6.6:", type=("build", "run"))
	depends_on("r-dexter@1.2.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-igraph@1.2.1:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
