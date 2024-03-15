# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeneoverlap(RPackage):
	"""Test and visualize gene overlaps

	Test two sets of gene lists and visualize the results.
	"""
	
	homepage = "http://shenlab-sinai.github.io/shenlab-sinai/"
	bioc = "GeneOverlap" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GeneOverlap_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GeneOverlap/GeneOverlap_1.38.0.tar.gz"]

	version("1.38.0", md5="0b5179a1183a82869935ca6c2c55aab3")

	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
