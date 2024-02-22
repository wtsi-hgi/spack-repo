# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFrailtysurv(RPackage):
	"""General Semiparametric Shared Frailty Model

	Simulates and fits semiparametric shared frailty models under a
    wide range of frailty distributions using a consistent and
    asymptotically-normal estimator. Currently supports: gamma, power variance
    function, log-normal, and inverse Gaussian frailty models.
	"""
	
	homepage = "https://github.com/vmonaco/frailtySurv/"
	cran = "frailtySurv" 

	version("1.3.8", md5="8e1d986f5b6d69d75c4e5c3a3dde1e53")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
