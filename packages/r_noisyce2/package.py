# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNoisyce2(RPackage):
	"""Cross-Entropy Optimisation of Noisy Functions

	Cross-Entropy optimisation of unconstrained deterministic and noisy
    functions illustrated in Rubinstein and Kroese (2004, ISBN:
    978-1-4419-1940-3) through a highly flexible and customisable function which 
    allows user to define custom variable domains, sampling distributions,
    updating and smoothing rules, and stopping criteria. Several built-in
    methods and settings make the package very easy-to-use under standard
    optimisation problems.
	"""
	
	homepage = "https://www.flaviosanti.it/software/noisyCE2"
	cran = "noisyCE2" 

	version("1.1.0", md5="d7e73d00d6919b534b07bb335192299b", url="https://cran.r-project.org/src/contrib/noisyCE2_1.1.0.tar.gz")

	depends_on("r-magrittr", type=("build", "run"))
