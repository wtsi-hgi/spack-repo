# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRemiod(RPackage):
	"""Reference-Based Multiple Imputation for Ordinal/Binary Response

	Reference-based multiple imputation of ordinal and binary responses under Bayesian
          framework, as described in Wang and Liu (2022) <arXiv:2203.02771>. Methods for 
          missing-not-at-random include Jump-to-Reference (J2R), Copy Reference (CR), and Delta 
          Adjustment which can generate tipping point analysis.
	"""
	
	homepage = "https://github.com/xsswang/remiod"
	cran = "remiod" 

	version("1.0.2", md5="47a205ab6a0374b29fdb55d82b385d17")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-jointai", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-dofuture", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ordinal", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mcmcse", type=("build", "run"))
	depends_on("jags", type=("build", "link", "run"))
