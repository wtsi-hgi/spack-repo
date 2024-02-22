# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCxr(RPackage):
	"""A Toolbox for Modelling Species Coexistence in R

	Recent developments in modern coexistence theory have
    advanced our understanding on how species are able to persist and
    co-occur with other species at varying abundances. However, applying
    this mathematical framework to empirical data is still challenging,
    precluding a larger adoption of the theoretical tools developed by
    empiricists. This package provides a complete toolbox for modelling
    interaction effects between species, and calculate fitness and niche
    differences.  The functions are flexible, may accept covariates, and
    different fitting algorithms can be used.  A full description of the
    underlying methods is available in García-Callejas, D., Godoy, O., and
    Bartomeus, I. (2020) <doi:10.1111/2041-210X.13443>.  Furthermore, the
    package provides a series of functions to calculate dynamics for
    stage-structured populations across sites.
	"""
	
	homepage = "https://github.com/RadicalCommEcol/cxr"
	cran = "cxr" 

	version("1.1.1", md5="f8cef535b89fc03b43eb3f61b4df64b6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
