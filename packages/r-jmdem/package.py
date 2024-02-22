# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJmdem(RPackage):
	"""Fitting Joint Mean and Dispersion Effects Models

	Joint mean and dispersion effects models fit the mean and dispersion parameters of a response variable by two separate linear models, the mean and dispersion submodels, simultaneously. It also allows the users to choose either the deviance or the Pearson residuals as the response variable of the dispersion submodel. Furthermore, the package provides the possibility to nest the submodels in one another, if one of the parameters has significant explanatory power on the other. Wu & Li (2016) <doi:10.1016/j.csda.2016.04.015>.
	"""
	
	cran = "jmdem" 

	version("1.0.1", md5="aff3f0b6759191e1ac640400c3f99f6e")

	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
