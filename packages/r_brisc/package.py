# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrisc(RPackage):
	"""Fast Inference for Large Spatial Datasets using BRISC

	Fits bootstrap with univariate spatial regression models using Bootstrap for Rapid Inference on Spatial Covariances (BRISC) for large datasets using nearest neighbor Gaussian processes detailed in Saha and Datta (2018) <doi:10.1002/sta4.184>.
	"""
	
	homepage = "https://github.com/ArkajyotiSaha/BRISC"
	cran = "BRISC" 

	version("1.0.5", md5="c82f874ae549ae510030a8c6735bccc2")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-rdist", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
