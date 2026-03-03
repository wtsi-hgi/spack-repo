# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMess(RPackage):
	"""Miscellaneous Esoteric Statistical Scripts

	A mixed collection of useful and semi-useful diverse
    statistical functions, some of which may even be referenced in
    The R Primer book.
	"""
	
	homepage = "https://github.com/ekstroem/MESS"
	cran = "MESS" 

	version("0.5.12", md5="1864ee5b8da022802f76520fd4754656")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-clipr", type=("build", "run"))
	depends_on("r-geepack", type=("build", "run"))
	depends_on("r-geem", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggformula", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-kinship2", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
