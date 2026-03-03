# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REzcutoffs(RPackage):
	"""Fit Measure Cutoffs in SEM

	Calculate cutoff values for model fit measures used in structural equation modeling (SEM) by simulating and testing data sets (cf. Hu & Bentler, 1999 <doi:10.1080/10705519909540118>) with the same parameters (population model, number of observations, etc.) as the model under consideration.
	"""
	
	cran = "ezCutoffs" 

	version("1.0.1", md5="b0733afa9efb697522f3ddd19e9b9fbd")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
