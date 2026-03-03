# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStarts(RPackage):
	"""Functions for the STARTS Model

	
    Contains functions for estimating the STARTS model of
    Kenny and Zautra (1995, 2001) <DOI:10.1037/0022-006X.63.1.52>,
    <DOI:10.1037/10409-008>. Penalized maximum likelihood
    estimation and Markov Chain Monte Carlo estimation are
    also provided, see Luedtke, Robitzsch and Wagner (2018) 
    <DOI:10.1037/met0000155>.
	"""
	
	homepage = "https://github.com/alexanderrobitzsch/STARTS"
	cran = "STARTS" 

	version("1.3-8", md5="1bd6ad0f7a79623905ed40c212b07030")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-cdm@7.1.19:", type=("build", "run"))
	depends_on("r-lam@0.3.27:", type=("build", "run"))
	depends_on("r-sirt@2.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
