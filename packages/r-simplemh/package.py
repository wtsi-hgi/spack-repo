# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimplemh(RPackage):
	"""Simple Metropolis-Hastings MCMC Algorithm

	A very bare-bones interface to use the Metropolis-Hastings Monte 
    Carlo Markov Chain algorithm. It is suitable for teaching and testing 
    purposes. 
	"""
	
	homepage = "https://github.com/Bisaloo/simpleMH"
	cran = "simpleMH" 

	version("0.1.1", md5="4080ca78c23cda0117e9ef89c6cb58c6")

	depends_on("r-mvtnorm", type=("build", "run"))
