# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStepjglm(RPackage):
	"""Variable Selection for Joint Modeling of Mean and Dispersion

	A Package for selecting variables for the joint modeling of mean and dispersion (including models for mixture experiments) based on hypothesis testing and the quality of model's fit. In each iteration of the selection process, a criterion for checking the goodness of fit is used as a filter for choosing the terms that will be evaluated by a hypothesis test. Pinto & Pereira (2021) <arXiv:2109.07978>.
	"""
	
	cran = "stepjglm" 

	version("0.0.1", md5="a041b5bbb7e98ea4c0d31f6152a059b1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rsq", type=("build", "run"))
