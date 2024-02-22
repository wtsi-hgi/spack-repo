# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAtemevs(RPackage):
	"""Average Treatment Effects with Measurement Error and Variable
Selection for Confounders

	A recent method proposed by Yi and Chen (2023) <doi:10.1177/09622802221146308> is used to estimate the average treatment effects using noisy data containing both measurement error and spurious variables. The package 'AteMeVs' contains a set of functions that provide a step-by-step estimation procedure, including the correction of the measurement error effects, variable selection for building the model used to estimate the propensity scores, and estimation of the average treatment effects. The functions contain multiple options for users to implement, including different ways to correct for the measurement error effects, distinct choices of penalty functions to do variable selection, and various regression models to characterize propensity scores.
	"""
	
	cran = "AteMeVs" 

	version("0.1.0", md5="f6dd8f42f0c0cd86fe9afaa7291ba76f")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ncvreg", type=("build", "run"))
