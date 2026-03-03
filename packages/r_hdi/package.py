# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdi(RPackage):
	"""High-Dimensional Inference

	Implementation of multiple approaches to perform inference in high-dimensional models.
	"""
	
	cran = "hdi" 

	version("0.1-9", md5="cf861f15d077dbdd1ef56890e9dc99f6")

	depends_on("r-scalreg", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-linprog", type=("build", "run"))
