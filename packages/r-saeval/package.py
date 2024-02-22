# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSaeval(RPackage):
	"""Small Area Estimation Evaluation

	Allows users to produce diagnostic procedures and graphic tools for the evaluation of Small Area estimators.
	"""
	
	cran = "SAEval" 

	version("1.0.0", md5="a8b6e04ce722320c306b2d7bbf347431")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggspatial", type=("build", "run"))
