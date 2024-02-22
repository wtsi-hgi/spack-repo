# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatentropy(RPackage):
	"""Spatial Entropy Measures

	The heterogeneity of spatial data presenting a finite number of categories can be measured via computation of spatial entropy. Functions are available for the computation of the main entropy and spatial entropy measures in the literature. They include the traditional version of Shannon's entropy (Shannon, 1948 <doi:10.1002/j.1538-7305.1948.tb01338.x>), Batty's spatial entropy (Batty, 1974 <doi:10.1111/j.1538-4632.1974.tb01014.x>), O'Neill's entropy (O'Neill et al., 1998 <doi:10.1007/BF00162741>), Li and Reynolds' contagion index (Li and Reynolds, 1993 <doi:10.1007/BF00125347>), Karlstrom and Ceccato's entropy (Karlstrom and Ceccato, 2002 <https://urn.kb.se/resolve?urn=urn:nbn:se:kth:diva-61351>), Leibovici's entropy (Leibovici, 2009 <doi:10.1007/978-3-642-03832-7_24>), Parresol and Edwards' entropy (Parresol and Edwards, 2014 <doi:10.3390/e16041842>) and Altieri's entropy (Altieri et al., 2018, <doi:10.1007/s10651-017-0383-1>). Full references for all measures can be found under the topic 'SpatEntropy'. The package is able to work with lattice and point data. The updated version works with the updated 'spatstat' package (>= 3.0-2). 
	"""
	
	cran = "SpatEntropy" 

	version("2.2-4", md5="38f6a9044a91b1573a31ceee4ca04d22")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-spatstat@3.0.2:", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat-random", type=("build", "run"))
