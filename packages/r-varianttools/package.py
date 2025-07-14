# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVarianttools(RPackage):
	"""Tools for Exploratory Analysis of Variant Calls

	Explore, diagnose, and compare variant calls using filters.
	"""
	
	bioc = "VariantTools"

	version("1.50.0", commit="79fdeffc99959be87f1d5ecfb4b7cb2e18f83fa6")
	version("1.44.0", commit="905b2d22c5e9416ce615a35f636ab83fa01058ad")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-s4vectors@0.17.33:", type=("build", "run"))
	depends_on("r-iranges@2.13.12:", type=("build", "run"))
	depends_on("r-genomicranges@1.31.8:", type=("build", "run"))
	depends_on("r-variantannotation@1.11.16:", type=("build", "run"))
	depends_on("r-rsamtools@1.31.2:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-genomicfeatures@1.31.3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rtracklayer@1.39.7:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
