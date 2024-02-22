# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlacksheepr(RPackage):
	"""Outlier Analysis for pairwise differential comparison

	Blacksheep is a tool designed for outlier analysis in the context of pairwise comparisons in an effort to find distinguishing characteristics from two groups. This tool was designed to be applied for biological applications such as phosphoproteomics or transcriptomics, but it can be used for any data that can be represented by a 2D table, and has two sub populations within the table to compare.
	"""
	
	bioc = "blacksheepr" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/blacksheepr_1.16.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/blacksheepr/blacksheepr_1.16.0.tar.gz"]

	version("1.16.0", md5="464b853300f0d97e2ad8f0a4188701c4")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-pasilla", type=("build", "run"))
