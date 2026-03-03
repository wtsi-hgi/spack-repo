# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMotmot(RPackage):
	"""Models of Trait Macroevolution on Trees

	Functions for fitting models of trait evolution
        on phylogenies for continuous traits. The majority of functions
        described in Thomas and Freckleton (2012) <doi:10.1111/j.2041-210X.2011.00132.x> 	and include functions that allow for tests of variation in the rates of trait evolution.
	"""
	
	homepage = "https://puttickbiology.wordpress.com/motmot/"
	cran = "motmot" 

	version("2.1.3", md5="a539d20aceb123ae1e5800aeb4a4443a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ape@3.0.7:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-caper", type=("build", "run"))
