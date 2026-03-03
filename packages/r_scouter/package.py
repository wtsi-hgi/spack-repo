# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScouter(RPackage):
	"""Simulate Controlled Outliers

	Using principal component analysis as a base model, 'SCOUTer' 
    offers a new approach to simulate outliers in a simple and precise way. 
    The user can generate new observations defining them by a pair of well-known 
    statistics: the Squared Prediction Error (SPE) and the Hotelling's T^2 (T^2) 
    statistics. Just by introducing the target values of the SPE and T^2, 'SCOUTer' 
    returns a new set of observations with the desired target properties. 
    Authors: Alba González, Abel Folch-Fortuny, Francisco Arteaga and 
    Alberto Ferrer (2020).
	"""
	
	cran = "SCOUTer" 

	version("1.0.0", md5="10ceb32a529f68ee87eb63dd4fd4855e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
