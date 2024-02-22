# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStepnorm(RPackage):
	"""Stepwise normalization functions for cDNA microarrays

	Stepwise normalization functions for cDNA microarray data.
	"""
	
	homepage = "http://www.biostat.ucsf.edu/jean/"
	bioc = "stepNorm" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/stepNorm_1.74.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/stepNorm/stepNorm_1.74.0.tar.gz"]

	version("1.74.0", md5="a8f357efcff85a6d723734d6e0a91ba0")

	depends_on("r@1.8:", type=("build", "run"))
	depends_on("r-marray", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
