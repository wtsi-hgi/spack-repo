# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcmcr(RPackage):
	"""Manipulate MCMC Samples

	Functions and classes to store, manipulate and summarise
    Monte Carlo Markov Chain (MCMC) samples. For more information see
    Brooks et al. (2011) <isbn:978-1-4200-7941-8>.
	"""
	
	homepage = "https://github.com/poissonconsulting/mcmcr"
	cran = "mcmcr" 

	version("0.6.1", md5="7285e7d677bfc5ebbc0ae6a337397b9c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-chk@0.7:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-extras", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-nlist", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-term", type=("build", "run"))
	depends_on("r-universals", type=("build", "run"))
