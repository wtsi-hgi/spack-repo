# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFmultivar(RPackage):
	"""Rmetrics - Modeling of Multivariate Financial Return
Distributions

	A collection of functions inspired by Venables and Ripley (2002) <doi:10.1007/978-0-387-21706-2>
             and Azzalini and Capitanio (1999) <arXiv:0911.2093> to manage, investigate and analyze
             bivariate and multivariate data sets of financial returns.
	"""
	
	homepage = "https://www.rmetrics.org"
	cran = "fMultivar" 

	version("4031.84", md5="6a4c832ca02230eea92b411e9d2c1c32")

	depends_on("r-fbasics", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-sn", type=("build", "run"))
