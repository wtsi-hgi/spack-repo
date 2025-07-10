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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/RUVnormalize_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/RUVnormalize/RUVnormalize_1.36.0.tar.gz"]

	version("1.36.0", sha256="89123363aaac11558e7126333f241a8f63e78b5ce7bea4c5f0f600b4e2fcaa2a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ruvnormalizedata", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
