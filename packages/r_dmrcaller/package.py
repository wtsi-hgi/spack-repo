# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDmrcaller(RPackage):
	"""Differentially Methylated Regions caller

	Uses Bisulfite sequencing data in two conditions and identifies differentially methylated regions between the conditions in CG and non-CG context. The input is the CX report files produced by Bismark and the output is a list of DMRs stored as GRanges objects.
	"""
	
	bioc = "DMRcaller" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/DMRcaller_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/DMRcaller/DMRcaller_1.34.0.tar.gz"]

	version("1.34.0", md5="1c5b37620b4950eb63e32c3063235e8e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors@0.23.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpproll", type=("build", "run"))
	depends_on("r-betareg", type=("build", "run"))
