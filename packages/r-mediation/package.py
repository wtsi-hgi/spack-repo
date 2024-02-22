# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMediation(RPackage):
	"""Causal Mediation Analysis

	We implement parametric and non parametric mediation analysis. This package performs the methods and suggestions in Imai, Keele and Yamamoto (2010) <DOI:10.1214/10-STS321>, Imai, Keele and Tingley (2010) <DOI:10.1037/a0020761>, Imai, Tingley and Yamamoto (2013) <DOI:10.1111/j.1467-985X.2012.01032.x>, Imai and Yamamoto (2013) <DOI:10.1093/pan/mps040> and Yamamoto (2013) <http://web.mit.edu/teppei/www/research/IVmediate.pdf>. In addition to the estimation of causal mediation effects, the software also allows researchers to conduct sensitivity analysis for certain parametric models.
	"""
	
	homepage = "https://imai.princeton.edu/projects/mechanisms.html"
	cran = "mediation" 

	version("4.5.0", md5="d41765c66464d7f13babf7b2761f48b9")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-lme4@1:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
