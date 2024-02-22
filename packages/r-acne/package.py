# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAcne(RPackage):
	"""Affymetrix SNP Probe-Summarization using Non-Negative Matrix
Factorization

	A summarization method to estimate allele-specific copy number signals for Affymetrix SNP microarrays using non-negative matrix factorization (NMF).
	"""
	
	homepage = "https://github.com/HenrikBengtsson/ACNE"
	cran = "ACNE" 

	version("0.9.1", md5="47d41a300777af2737de9485dcd95444")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-aroma-affymetrix@2.14:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-r-methodss3@1.7:", type=("build", "run"))
	depends_on("r-r-oo@1.23:", type=("build", "run"))
	depends_on("r-r-utils@2.1:", type=("build", "run"))
	depends_on("r-matrixstats@0.50:", type=("build", "run"))
	depends_on("r-r-filesets@2.9:", type=("build", "run"))
	depends_on("r-aroma-core@2.14:", type=("build", "run"))
