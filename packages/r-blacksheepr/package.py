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

	version("1.22.0", commit="b3b2a6d375b1c418771e357a85e2052578438886")
	version("1.16.0", commit="9445c8fdeac119f5e5e5eddcaad738e11f6ba022")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-pasilla", type=("build", "run"))
