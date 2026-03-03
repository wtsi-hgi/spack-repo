# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmfor(RPackage):
	"""Functions for Forest Biometrics

	Functions for different purposes related to forest biometrics, including illustrative graphics, numerical computation, modeling height-diameter relationships, prediction of tree volumes, modelling of diameter distributions and estimation off stand density using ITD. Several empirical datasets are also included. 
	"""
	
	cran = "lmfor" 

	version("1.6", md5="3f112a0d9e4205d70b1e2f0442c8e313")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-spatstat", type=("build", "run"))
	depends_on("r-magic", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
