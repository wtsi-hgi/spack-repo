# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConcur(RPackage):
	"""Copy Number Profile Curve-Based Association Test

	Implements a kernel-based association test for copy number 
  variation (CNV) aggregate analysis
  in a certain genomic region (e.g., gene set, chromosome, or genome) that is
  robust to the within-locus and across-locus etiological heterogeneity, and 
  bypass the need to define a "locus" unit for CNVs. 
  Brucker, A., et al. (2020) <doi:10.1101/666875>.
	"""
	
	cran = "CONCUR" 

	version("1.4", md5="68e601e21e0767db631c8c18725461ea")

	depends_on("r-compquadform", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
