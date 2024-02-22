# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUbl(RPackage):
	"""An Implementation of Re-Sampling Approaches to Utility-Based
Learning for Both Classification and Regression Tasks

	Provides a set of functions that can be used to obtain better predictive performance on cost-sensitive and cost/benefits tasks (for both regression and classification). This includes re-sampling approaches that modify the original data set biasing it towards the user preferences.
	"""
	
	homepage = "https://github.com/paobranco/UBL"
	cran = "UBL" 

	version("0.0.9", md5="eed596b808757184285d5ad55f71940f")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mba", type=("build", "run"))
	depends_on("r-gstat", type=("build", "run"))
	depends_on("r-automap", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
