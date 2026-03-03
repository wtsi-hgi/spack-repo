# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpass(RPackage):
	"""Study Planning and Adaptation of Sample Size

	Sample size estimation and blinded sample size reestimation in Adaptive Study Design.
	"""
	
	cran = "spass" 

	version("1.3", md5="96739e44de4ef8520cfdf23c071aa8f1")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-geepack", type=("build", "run"))
