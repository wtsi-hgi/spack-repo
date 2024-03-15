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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GSReg_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GSReg/GSReg_1.36.0.tar.gz"]

	version("1.36.0", md5="631e2589b571bfcdf38b5673ba0693d0")

	depends_on("r@2.13.1:", type=("build", "run"))
	depends_on("r-homo-sapiens", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
