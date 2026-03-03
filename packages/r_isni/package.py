# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsni(RPackage):
	"""Index of Local Sensitivity to Nonignorability

	The current version provides functions to compute, print and summarize the Index of Sensitivity to Nonignorability (ISNI) in the generalized linear model for independent data, and in the marginal multivariate Gaussian model and the mixed-effects models for continuous and binary longitudinal/clustered data. It allows for arbitrary patterns of missingness in the regression outcomes  caused by dropout and/or intermittent missingness. One can compute the sensitivity index without estimating any nonignorable models or positing specific magnitude of nonignorability. Thus ISNI provides a simple quantitative assessment of how robust the standard estimates assuming missing at random  is with respect to the assumption of ignorability. For a tutorial, download at <https://huixie.people.uic.edu/Research/ISNI_R_tutorial.pdf>.	For more details, see Troxel Ma and Heitjan (2004) and Xie and Heitjan (2004) <doi:10.1191/1740774504cn005oa> and Ma Troxel and Heitjan (2005) <doi:10.1002/sim.2107> and  Xie (2008) <doi:10.1002/sim.3117> and  Xie (2012) <doi:10.1016/j.csda.2010.11.021> and Xie and Qian (2012) <doi:10.1002/jae.1157>.
	"""
	
	cran = "isni" 

	version("1.3", md5="7c3372aa8db9add383d8e0cfbcf02e28")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
