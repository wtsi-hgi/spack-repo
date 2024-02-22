# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNormqpcr(RPackage):
	"""Functions for normalisation of RT-qPCR data

	Functions for the selection of optimal reference genes and the normalisation of real-time quantitative PCR data.
	"""
	
	homepage = "www.bioconductor.org/packages/release/bioc/html/NormqPCR.html"
	bioc = "NormqPCR" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/NormqPCR_1.48.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/NormqPCR/NormqPCR_1.48.0.tar.gz"]

	version("1.48.0", md5="379e7395ad03c0d57dffa7331748e253")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-readqpcr", type=("build", "run"))
	depends_on("r-qpcr", type=("build", "run"))
