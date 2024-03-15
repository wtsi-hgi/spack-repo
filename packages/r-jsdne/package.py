# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJsdne(RPackage):
	"""Estimating the Age using Auricular Surface by DNE

	The age is estimated by calculating the Dirichlet Normal Energy (DNE) on the whole auricular surface and the apex of the auricular surface. It involves three estimation methods: principal component discriminant analysis (PCQDA), principal component regression analysis (PCR), and principal component logistic regression analysis (PCLR) methods. The package is created with the data from the Louis Lopes Collection in Lisbon, the 21st Century Identified Human Remains Collection in Coimbra, and the CAL Milano Cemetery Skeletal Collection in Milan. 
	"""
	
	cran = "JSDNE" 

	version("4.2.2", md5="73e72e0fd244aecfad37bee338334099")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-molar", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-rvcg", type=("build", "run"))
