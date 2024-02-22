# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayess(RPackage):
	"""Bayesian Essentials with R

	Allows the reenactment of the R programs used in 
        the book Bayesian Essentials with R without further programming. 
        R code being available as well, they can be modified by the user
        to conduct one's own simulations. 
	    Marin J.-M. and Robert C. P. (2014) <doi:10.1007/978-1-4614-8687-9>.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "bayess" 

	version("1.5", md5="d3b8145ae7baf2d79e365683cc11fbc1")

	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
