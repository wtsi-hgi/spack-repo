# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRuvnormalize(RPackage):
	"""RUV for normalization of expression array data

	RUVnormalize is meant to remove unwanted variation from gene expression data when the factor of interest is not defined, e.g., to clean up a dataset for general use or to do any kind of unsupervised analysis.
	"""
	
	bioc = "RUVnormalize" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/RUVnormalize_1.36.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/RUVnormalize/RUVnormalize_1.36.0.tar.gz"]

	version("1.36.0", md5="2d5d0d40d8720734dee3f8dc437c0756")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ruvnormalizedata", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
