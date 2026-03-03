# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCountr(RPackage):
	"""Flexible Univariate Count Models Based on Renewal Processes

	Flexible univariate count models based on renewal processes. The
    models may include covariates and can be specified with familiar formula
    syntax as in glm() and package 'flexsurv'.  The methodology is described by
    Kharrat et all (2019) <doi:10.18637/jss.v090.i13> (included as vignette
    'Countr_guide' in the package).
    If the suggested package 'pscl' is not available from CRAN, it can be
    installed with 'remotes::install_github("cran/pscl")'. It is no longer used
    by the functions in this package but is needed for some of the extended
    examples.
	"""
	
	homepage = "https://geobosh.github.io/Countr/"
	cran = "Countr" 

	version("3.5.8", md5="366b1e5c545962840def32162910b9da")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-flexsurv", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-rdpack@0.7.0:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-standardize", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
