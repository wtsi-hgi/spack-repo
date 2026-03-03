# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParamtest(RPackage):
	"""Run a Function Iteratively While Varying Parameters

	Run simulations or other functions while easily varying parameters
    from one iteration to the next. Some common use cases would be grid search
    for machine learning algorithms, running sets of simulations (e.g.,
    estimating statistical power for complex models), or bootstrapping under
    various conditions. See the 'paramtest' documentation for more information
    and examples.
	"""
	
	cran = "paramtest" 

	version("0.1.0", md5="469300d7d0f2328367bb8d7d9071264f")

	depends_on("r-boot", type=("build", "run"))
