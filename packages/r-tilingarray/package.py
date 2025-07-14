# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTilingarray(RPackage):
	"""Transcript mapping with high-density oligonucleotide tiling arrays

	The package provides functionality that can be useful for the analysis of high-density tiling microarray data (such as from Affymetrix genechips) for measuring transcript abundance and architecture. The main functionalities of the package are: 1. the class 'segmentation' for representing partitionings of a linear series of data; 2. the function 'segment' for fitting piecewise constant models using a dynamic programming algorithm that is both fast and exact; 3. the function 'confint' for calculating confidence intervals using the strucchange package; 4. the function 'plotAlongChrom' for generating pretty plots; 5. the function 'normalizeByReference' for probe-sequence dependent response adjustment from a (set of) reference hybridizations.
	"""
	
	bioc = "tilingArray"

	version("1.86.0", commit="7170d5f5e13be2621743e6c2d255b7f9213e4e9b")
	version("1.80.0", commit="338250205f4ab8d1da3a0f8738a04605703b8c18")

	depends_on("r@2.11:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-pixmap", type=("build", "run"))
	depends_on("r-strucchange", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-vsn", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
