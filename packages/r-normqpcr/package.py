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

	version("1.54.0", commit="fffd9b85e0963769a8b5e45b34a9eaf04426145c")
	version("1.48.0", commit="d7417f3f7a3897079327b3346f3fd467f07441ca")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-readqpcr", type=("build", "run"))
	depends_on("r-qpcr", type=("build", "run"))
