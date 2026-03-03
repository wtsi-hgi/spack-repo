# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpcosa(RPackage):
	"""Spatial Coverage Sampling and Random Sampling from Compact
Geographical Strata

	Spatial coverage sampling and random sampling from compact
        geographical strata created by k-means. See Walvoort et al. (2010) 
        <doi:10.1016/j.cageo.2010.04.005> for details. 
	"""
	
	homepage = "https://git.wur.nl/Walvo001/spcosa"
	cran = "spcosa" 

	version("0.4-2", md5="7963b0b25bb556df25732e49f06abab3")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rjava@1.0.0:", type=("build", "run"))
	depends_on("r-sp@1.4.6:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("openjdk@1.6:", type=("build", "link", "run"))
