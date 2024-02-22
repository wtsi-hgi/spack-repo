# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFreesortr(RPackage):
	"""Free Sorting Data Analysis

	Provides tools for describing and analysing free sorting data. Main methods are computation of consensus partition and factorial analysis of the dissimilarity matrix between stimuli (using multidimensional scaling approach).
	"""
	
	cran = "FreeSortR" 

	version("1.3", md5="04c5148f6345927ca2df9be5e6d751f7")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-smacof", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
