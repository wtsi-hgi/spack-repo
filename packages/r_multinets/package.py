# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultinets(RPackage):
	"""Multilevel Networks Analysis

	Analyze multilevel networks as described in Lazega et al (2008)
    <doi:10.1016/j.socnet.2008.02.001> and in Lazega and Snijders 
    (2016, ISBN:978-3-319-24520-1). The package was developed essentially as an 
    extension to 'igraph'.
	"""
	
	homepage = "https://github.com/neylsoncrepalde/multinets"
	cran = "multinets" 

	version("0.2.2", md5="6bd9f5e8d289875d1fc428049b5e88c9")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
