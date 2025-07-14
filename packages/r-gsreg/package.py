# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsreg(RPackage):
	"""Gene Set Regulation (GS-Reg)

	A package for gene set analysis based on the variability of expressions as well as a method to detect Alternative Splicing Events . It implements DIfferential RAnk Conservation (DIRAC) and gene set Expression Variation Analysis (EVA) methods. For detecting Differentially Spliced genes, it provides an implementation of the Spliced-EVA (SEVA).
	"""
	
	bioc = "GSReg"

	version("1.42.0", commit="32b2332f1165083d3c4e571e8599a44b39ea952c")
	version("1.36.0", commit="986592f073d39ec5784b9a1383c420daa7573e0a")

	depends_on("r@2.13.1:", type=("build", "run"))
	depends_on("r-homo-sapiens", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
