# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSingscore(RPackage):
	"""Rank-based single-sample gene set scoring method

	A simple single-sample gene signature scoring method that uses rank-based statistics to analyze the sample's gene expression profile. It scores the expression activities of gene sets at a single-sample level.
	"""
	
	homepage = "https://davislaboratory.github.io/singscore"
	bioc = "singscore" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/singscore_1.22.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/singscore/singscore_1.22.0.tar.gz"]

	version("1.22.0", md5="c3ab598fd61c5bb54a842f9738133d24")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-gseabase", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
