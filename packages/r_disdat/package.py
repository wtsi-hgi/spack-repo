# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDisdat(RPackage):
	"""Data for Comparing Species Distribution Modeling Methods

	Easy access to species distribution data for 6 regions in the world, for a total of 226 anonymised species. These data are described and made available by Elith et al (2020) <doi:10.17161/bi.v15i2.13384> to compare species distribution modelling methods. 
	"""
	
	cran = "disdat" 

	version("1.0-1", md5="fb1654c2695ddc5ce4b257129735ddf8")

	depends_on("r@3.5:", type=("build", "run"))
