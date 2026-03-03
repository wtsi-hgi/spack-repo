# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhylosem(RPackage):
	"""Phylogenetic Structural Equation Model

	Applies phylogenetic comparative methods (PCM) and phylogenetic trait imputation using 
    structural equation models (SEM), extending methods from Thorson et al. (2023) <doi:10.1111/2041-210X.14076>.  
    This implementation includes a minimal set of features, to 
    allow users to easily read all of the documentation and source code.  PCM using SEM 
    includes phylogenetic linear models and structural equation models as nested submodels, 
    but also allows imputation of missing values.  Features and comparison with other packages
    are described in Thorson and van der Bijl (2023) <doi:10.1111/jeb.14234>. 
	"""
	
	homepage = "https://james-thorson-noaa.github.io/phylosem/"
	cran = "phylosem" 

	version("1.1.4", md5="c1b12873e2a57352a268a75915136eb3")
	version("1.1.3", md5="d32dcbcb0d8b73338e80affed1dcd09c")

	depends_on("r-tmb", type=("build", "run"))
	depends_on("r@4:", type=("build", "run"))
	depends_on("r-sem", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-phylobase", type=("build", "run"))
	depends_on("r-phylopath", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
