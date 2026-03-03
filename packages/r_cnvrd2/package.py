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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CNVrd2_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CNVrd2/CNVrd2_1.40.0.tar.gz"]

	version("1.40.0", md5="9cc2c933a0a521472b5eb6f1382cefd5", url="https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CNVrd2_1.40.0.tar.gz")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-dnacopy", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
