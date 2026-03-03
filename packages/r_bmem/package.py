# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBmem(RPackage):
	"""Mediation Analysis with Missing Data Using Bootstrap

	Four methods for mediation analysis with missing data: Listwise deletion, Pairwise deletion, Multiple imputation, and Two Stage Maximum Likelihood algorithm. For MI and TS-ML, auxiliary variables can be included. Bootstrap confidence intervals for mediation effects are obtained. The robust method is also implemented for TS-ML. Since version 1.4, bmem adds the capability to conduct power analysis for mediation models. Details about the methods used can be found in these articles. Zhang and Wang (2003) <doi:10.1007/s11336-012-9301-5>. Zhang (2014) <doi:10.3758/s13428-013-0424-0>.
	"""
	
	homepage = "https://bigdatalab.nd.edu"
	cran = "bmem" 

	version("2.1", md5="ec597c11cd89e40496d67f5a8fa4f4f8")

	depends_on("r@1.7:", type=("build", "run"))
	depends_on("r-amelia", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-snowfall", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-sem", type=("build", "run"))
