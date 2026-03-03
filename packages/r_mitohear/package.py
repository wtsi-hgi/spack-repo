# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMitohear(RPackage):
	"""Quantification of Mitochondrial DNA Heteroplasmy

	Allows the estimation and downstream statistical analysis of the mitochondrial DNA Heteroplasmy calculated from single-cell datasets <https://github.com/ScialdoneLab/MitoHEAR/tree/master>.
	"""
	
	cran = "MitoHEAR" 

	version("0.1.0", md5="93112767f5621306dc7bf12f22db6629")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-dynamictreecut", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mcclust", type=("build", "run"))
	depends_on("r-rdist", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
