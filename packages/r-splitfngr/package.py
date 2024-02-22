# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSplitfngr(RPackage):
	"""Combined Evaluation and Split Access of Functions

	
  Some R functions, such as optim(), require a function
  its gradient passed as separate arguments. When these are
  expensive to calculate it may be much faster to calculate
  the function (fn) and gradient (gr) together since they often share
  many calculations (chain rule). This package allows the user
  to pass in a single function that returns both the function
  and gradient, then splits (hence 'splitfngr') them
  so the results can be accessed
  separately. The functions provided allow this to be done with
  any number of functions/values, not just for functions and gradients.
	"""
	
	cran = "splitfngr" 

	version("0.1.2", md5="4d3c8ce3c97421c9c8768026307988d0")

	depends_on("r-lbfgs", type=("build", "run"))
