# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSynthtools(RPackage):
	"""Tools and Tests for Experiments with Partially Synthetic Data
Sets

	A set of functions to support experimentation in the utility of partially synthetic data sets.  All functions compare an observed data set to one or a set of partially synthetic data sets derived from the observed data to (1) check that data sets have identical attributes, (2) calculate overall and specific variable perturbation rates, (3) check for potential logical inconsistencies, and (4) calculate confidence intervals and standard errors of desired variables in multiple imputed data sets. Confidence interval and standard error formulas have options for either synthetic data sets or multiple imputed data sets. For more information on the formulas and methods used, see Reiter & Raghunathan (2007) <doi:10.1198/016214507000000932>.
	"""
	
	cran = "SynthTools" 

	version("1.0.1", md5="d129c8bc322e1eab7b90654f28e3497c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
