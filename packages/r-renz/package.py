# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRenz(RPackage):
	"""R-Enzymology

	Contains utilities for the analysis of Michaelian kinetic data. Beside the classical linearization 
	methods (Lineweaver-Burk, Eadie-Hofstee, Hanes-Woolf and Eisenthal-Cornish-Bowden), features include the 
	ability to carry out weighted regression analysis that, in most cases, substantially improves the estimation 
	of kinetic parameters (Aledo (2021) <doi:10.1002/bmb.21522>). To avoid data transformation and the potential
	biases introduced by them, the package also offers functions to directly fitting data to the Michaelis-Menten 
	equation, either using ([S], v) or (time, [S]) data. Utilities to simulate substrate progress-curves (making 
	use of the Lambert W function) are also provided. The package is accompanied of vignettes that aim to orientate
	the user in the choice of the most suitable method to estimate the kinetic parameter of an Michaelian enzyme.
	"""
	
	cran = "renz" 

	version("0.2.1", md5="60d1e9050b75a6f7991f56d8d069d5ef")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
