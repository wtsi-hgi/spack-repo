# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRandomforestsgls(RPackage):
	"""Random Forests for Dependent Data

	Fits non-linear regression models on dependant data with Generalised Least Square (GLS) based Random Forest (RF-GLS) detailed in Saha, Basu and Datta (2020) <arXiv:2007.15421>.
	"""
	
	homepage = "https://github.com/ArkajyotiSaha/RandomForestsGLS"
	cran = "RandomForestsGLS" 

	version("0.1.4", md5="3b71ad22dbde89c5f81a38d85ad6bdf3")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-brisc", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
