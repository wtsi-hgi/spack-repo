# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCnvrd2(RPackage):
	"""CNVrd2: a read depth-based method to detect and genotype complex common copy number variants from next generation sequencing data.

	CNVrd2 uses next-generation sequencing data to measure human gene copy number for multiple samples, indentify SNPs tagging copy number variants and detect copy number polymorphic genomic regions.
	"""
	
	homepage = "https://github.com/hoangtn/CNVrd2"
	bioc = "CNVrd2"

	version("1.46.0", commit="a9e11c47d973d7007a502c23bebbaa34542f59ff")
	version("1.40.0", commit="497de63b2ef1328821b2d5873fb62f99cdabe1cc")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-dnacopy", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
