# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHicvenndiagram(RPackage):
	"""Venn Diagram for genomic interaction data

	A package to generate high-resolution Venn and Upset plots for genomic interaction data from HiC, ChIA-PET, HiChIP, PLAC-Seq, Hi-TrAC, HiCAR and etc. The package generates plots specifically crafted to eliminate the deceptive visual representation caused by the counts method.
	"""
	
	homepage = "https://github.com/jianhong/hicVennDiagram"
	bioc = "hicVennDiagram" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/hicVennDiagram_1.0.2.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/hicVennDiagram/hicVennDiagram_1.0.2.tar.gz"]

	version("1.0.2", md5="61651aeae22cb23e4e66b3a7b9d0896f")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-interactionset", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-complexupset", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-eulerr", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-svglite", type=("build", "run"))
