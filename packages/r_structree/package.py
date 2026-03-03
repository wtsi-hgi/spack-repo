# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStructree(RPackage):
	"""Tree-Structured Clustering

	Tree-structured modelling of categorical predictors (Tutz and Berger (2018), <doi:10.1007/s11634-017-0298-6>) or measurement
    units (Berger and Tutz (2018), <doi:10.1080/10618600.2017.1371030>).
	"""
	
	cran = "structree" 

	version("1.1.7", md5="85dad195a8da8688bc4f3e2d8e0d3e43")

	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-penalized", type=("build", "run"))
