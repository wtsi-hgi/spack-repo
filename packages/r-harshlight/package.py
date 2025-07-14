# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHarshlight(RPackage):
	"""A "corrective make-up" program for microarray chips

	The package is used to detect extended, diffuse and compact blemishes on microarray chips. Harshlight automatically marks the areas in a collection of chips (affybatch objects) and a corrected AffyBatch object is returned, in which the defected areas are substituted with NAs or the median of the values of the same probe in the other chips in the collection. The new version handle the substitute value as whole matrix to solve the memory problem.
	"""
	
	homepage = "http://asterion.rockefeller.edu/Harshlight/"
	bioc = "Harshlight"

	version("1.80.0", commit="9a7ef7428d64ac6573744fd4b67acf339442b372")
	version("1.74.0", commit="c397a39aa9779f7343c700208572a512ad06c4a4")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-altcdfenvs", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
