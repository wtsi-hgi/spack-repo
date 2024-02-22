# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTag(RPackage):
	"""Transformed Additive Gaussian Processes

	Implement the transformed additive Gaussian (TAG) process and the  transformed approximately additive Gaussian (TAAG) process proposed in Lin and Joseph (2020) <DOI:10.1080/00401706.2019.1665592>. These functions can be used to model deterministic computer experiments, obtain predictions at new inputs, and quantify the uncertainty of the predictions. This research is supported by a U.S. National Science Foundation grant DMS-1712642 and a U.S. Army Research Office grant W911NF-17-1-0007.
	"""
	
	cran = "TAG" 

	version("0.5.1", md5="806e4161c67c8283978f58b01196f8f0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-dicekriging", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-fastgp", type=("build", "run"))
	depends_on("r-mlegp", type=("build", "run"))
	depends_on("r-randtoolbox", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
