# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSstack(RPackage):
	"""Bootstrap Stacking of Random Forest Models for Heterogeneous
Data

	Generates and predicts a set of linearly stacked Random Forest models using bootstrap sampling. Individual datasets may be heterogeneous (not all samples have full sets of features). Contains support for parallelization but the user should register their cores before running. This is an extension of the method found in Matlock (2018) <doi:10.1186/s12859-018-2060-2>.
	"""
	
	cran = "Sstack" 

	version("1.0.1", md5="3989f78574ded5b70a17f6bf7cca0dd5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
