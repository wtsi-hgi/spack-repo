# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJagshelper(RPackage):
	"""Extracting and Visualizing Output from 'jagsUI'

	Tools are provided to streamline Bayesian analyses in 'JAGS' using 
    the 'jagsUI' package.  Included are functions for extracting output in 
    simpler format, functions for streamlining assessment of convergence, and 
    functions for producing summary plots of output.  Also included is a 
    function that provides a simple template for running 'JAGS' from 'R'.
    Referenced materials can be found at <DOI:10.1214/ss/1177011136>.
	"""
	
	homepage = "https://github.com/mbtyers/jagshelper"
	cran = "jagshelper" 

	version("0.2.2", md5="7ae631d683e55723c7cd68d471eecb36")
	version("0.2.1", md5="d26333cff2bac778672cc38e42373253")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-jagsui", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
