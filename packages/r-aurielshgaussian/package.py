# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAurielshgaussian(RPackage):
	"""Creates a Neighbourhood Using Locality Sensitive Hashing for
Gaussian Projections

	Uses locality sensitive hashing and creates a neighbourhood graph for a data set and calculates the adjusted rank index value for the same. It uses Gaussian random planes to decide the nature of a given point. Datar, Mayur, Nicole Immorlica, Piotr Indyk, and Vahab S. Mirrokni(2004) <doi:10.1145/997817.997857>.
	"""
	
	cran = "AurieLSHGaussian" 

	version("0.2.0", md5="31686e411174ed2695e0e3f2c3ba0496")

	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-lsa", type=("build", "run"))
	depends_on("r-flexclust", type=("build", "run"))
