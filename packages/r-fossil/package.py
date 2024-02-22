# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFossil(RPackage):
	"""Palaeoecological and Palaeogeographical Analysis Tools

	A set of analytical tools useful in analysing ecological and geographical data sets, both ancient and modern. The package includes functions for estimating species richness (Chao 1 and 2, ACE, ICE, Jacknife), shared species/beta diversity, species area curves and geographic distances and areas.
	"""
	
	homepage = "http://matthewvavrek.com/programs-and-code/fossil/"
	cran = "fossil" 

	version("0.4.0", md5="35bcc5487e1671d5b376429c9ba59738")

	depends_on("r-sp", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-shapefiles", type=("build", "run"))
