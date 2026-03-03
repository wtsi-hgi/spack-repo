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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Harshlight_1.74.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Harshlight/Harshlight_1.74.0.tar.gz"]

	version("1.74.0", md5="36adabb3111ae035069431431dd9434a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-altcdfenvs", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
