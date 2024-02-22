# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMero(RPackage):
	"""Performing Monte Carlo Expectation Maximization Random Forest
Imputation for Biological Data

	Perform missing value imputation for biological data using the random forest algorithm, the imputation aim to keep the original mean and standard deviation consistent after imputation.
	"""
	
	cran = "MERO" 

	version("0.1.2", md5="45bbe822a823f98d548bb45acf6bf6b9")

	depends_on("r-missforest", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
