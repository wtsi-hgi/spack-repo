# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLongiturf(RPackage):
	"""Random Forests for Longitudinal Data

	Random forests are a statistical learning method widely used in many areas of scientific research essentially for its ability to learn complex relationships between input and output variables and also its capacity to handle high-dimensional data. However, current random forests approaches are not flexible enough to handle longitudinal data.  In this package, we propose a general approach of random forests for high-dimensional longitudinal data. It includes a flexible stochastic model which allows the covariance structure to vary over time. Furthermore, we introduce a new method which takes intra-individual covariance into consideration to build random forests. The method is fully detailled in Capitaine et.al. (2020) <doi:10.1177/0962280220946080> Random forests for high-dimensional longitudinal data.
	"""
	
	cran = "LongituRF" 

	version("0.9", md5="43bdd13103c9079340d9e96e7bd44ac9")

	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-latex2exp", type=("build", "run"))
