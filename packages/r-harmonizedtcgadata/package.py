# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHarmonizedtcgadata(RPackage):
	"""Processed Harmonized TCGA Data of Five Selected Cancer Types

	This package contains the processed harmonized TCGA data of five cancer types used in "Tianle Ma and Aidong Zhang, Integrate Multi-omic Data Using Affinity Network Fusion (ANF) for Cancer Patient Clustering".
	"""
	
	bioc = "HarmonizedTCGAData"

	version("1.30.0", commit="38e15e3709e479cc70da2d7642933a1ea5cbae91")
	version("1.24.0", commit="331c38b41dbd0bcb84f2a263093144b9ec98b3d3")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))

