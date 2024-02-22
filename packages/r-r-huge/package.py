# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRHuge(RPackage):
	"""Methods for Accessing Huge Amounts of Data [deprecated]

	DEPRECATED. Do not start building new projects based on this package. Cross-platform alternatives are the following packages: bigmemory (CRAN), ff (CRAN), BufferedMatrix (Bioconductor).  The main usage of it was inside the aroma.affymetrix package. (The package currently provides a class representing a matrix where the actual data is stored in a binary format on the local file system.  This way the size limit of the data is set by the file system and not the memory.)
	"""
	
	homepage = "https://github.com/HenrikBengtsson/R.huge"
	cran = "R.huge" 

	version("0.10.1", md5="686fae5d59823061bcde86bd8ba8bd3d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-r-methodss3@1.7:", type=("build", "run"))
	depends_on("r-r-oo@1.23:", type=("build", "run"))
	depends_on("r-r-utils@1.34:", type=("build", "run"))
