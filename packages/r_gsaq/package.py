# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsaq(RPackage):
	"""Gene Set Analysis with QTL

	Computation of Quantitative Trait Loci hits in the selected gene set. Performing gene set validation with Quantitative Trait Loci information. Performing gene set enrichment analysis with available Quantitative Trait Loci data and computation of statistical significance value from gene set analysis. Obtaining the list of Quantitative Trait Loci hit genes along with their overlapped Quantitative Trait Loci names.
	"""
	
	cran = "GSAQ" 

	version("1.0", md5="980d2dc54b91b70cf27c026f89b1f0b8")

	depends_on("r@3.3.1:", type=("build", "run"))
