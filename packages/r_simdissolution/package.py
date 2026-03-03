# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimdissolution(RPackage):
	"""Modeling and Assessing Similarity of Drug Dissolutions Profiles

	Implementation of a model-based bootstrap approach for testing whether two formulations are similar. The package provides a function for fitting a pharmacokinetic model to time-concentration data and comparing the results for all five candidate models regarding the Residual Sum of Squares (RSS). The candidate set contains a First order, Hixson-Crowell, Higuchi, Weibull and a logistic model. The assessment of similarity implemented in this package is performed regarding the maximum deviation of the profiles. See Moellenhoff et al. (2018) <doi:10.1002/sim.7689> for details.
	"""
	
	cran = "SimDissolution" 

	version("0.1.0", md5="cb9e018940d0b2fe57fca8fb71841f56")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-alabama", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
