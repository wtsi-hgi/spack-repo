# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMacsr(RPackage):
	"""MACS: Model-based Analysis for ChIP-Seq

	The Model-based Analysis of ChIP-Seq (MACS) is a widely used toolkit for identifying transcript factor binding sites. This package is an R wrapper of the lastest MACS3.
	"""
	
	bioc = "MACSr" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/MACSr_1.10.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/MACSr/MACSr_1.10.0.tar.gz"]

	version("1.10.0", md5="bab4dacc8d41a2a47798bc740181f014")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-basilisk", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
