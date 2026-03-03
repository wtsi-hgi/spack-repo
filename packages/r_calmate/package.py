# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCalmate(RPackage):
	"""Improved Allele-Specific Copy Number of SNP Microarrays for
Downstream Segmentation

	The CalMaTe method calibrates preprocessed allele-specific copy number estimates (ASCNs) from DNA microarrays by controlling for single-nucleotide polymorphism-specific allelic crosstalk. The resulting ASCNs are on average more accurate, which increases the power of segmentation methods for detecting changes between copy number states in tumor studies including copy neutral loss of heterozygosity. CalMaTe applies to any ASCNs regardless of preprocessing method and microarray technology, e.g. Affymetrix and Illumina.
	"""
	
	homepage = "https://github.com/HenrikBengtsson/calmate/"
	cran = "calmate" 

	version("0.13.0", md5="47d7d97c11800106fecc6c1fe5ebca1e")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-r-utils@2.11:", type=("build", "run"))
	depends_on("r-aroma-core@3.2.2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-r-methodss3@1.8.1:", type=("build", "run"))
	depends_on("r-r-oo@1.24:", type=("build", "run"))
	depends_on("r-matrixstats@0.61:", type=("build", "run"))
	depends_on("r-r-filesets@2.14:", type=("build", "run"))
