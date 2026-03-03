# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCvwrapr(RPackage):
	"""Tools for Cross Validation

	Tools for performing cross-validation (CV). The main function is a 
    general purpose wrapper that performs k-fold CV for any tuning parameter in 
    any supervised learning method. The package also has a function that 
    computes the loss incurred by a set of predictions for a variety of loss 
    functions and model families.
	"""
	
	cran = "cvwrapr" 

	version("1.0", md5="7de15e67b9dd250b614a140f0e5eea86")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
