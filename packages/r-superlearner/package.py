# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSuperlearner(RPackage):
	"""Super Learner Prediction

	Implements the super learner prediction method and contains a
    library of prediction algorithms to be used in the super learner.
	"""
	
	homepage = "https://github.com/ecpolley/SuperLearner"
	cran = "SuperLearner" 

	version("2.0-29", md5="8bed600a31204f2fa3f4588a140a0344")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-nnls", type=("build", "run"))
	depends_on("r-gam@1.15:", type=("build", "run"))
	depends_on("r-cvauc", type=("build", "run"))
