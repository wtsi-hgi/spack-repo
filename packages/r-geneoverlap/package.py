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

	version("1.44.0", tag="RELEASE_3_21")
	version("1.38.0", sha256="fc7e3b2fef8a07b78a9a4ad2f45ccac6bf9cd2054ac74865ef086af46d1c8d1c")

	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
