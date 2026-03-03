# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaaper(RPackage):
	"""Analysis of Alternative Polyadenylation Using 3' End-Linked
Reads

	A computational method developed for model-based analysis of alternative polyadenylation (APA) using 3' end-linked reads. It accurately assigns 3' RNA-seq reads to polyA sites through statistical modeling, and generates multiple statistics for APA analysis. Please also see Li WV, Zheng D, Wang R, Tian B (2021) <doi:10.1186/s13059-021-02429-5>.
	"""
	
	homepage = "https://github.com/Vivianstats/MAAPER"
	cran = "MAAPER" 

	version("1.1.1", md5="af4f0a544843cff842c7d8bd813c6aa0")

	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
