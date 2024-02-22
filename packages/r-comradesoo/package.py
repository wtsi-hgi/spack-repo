# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComradesoo(RPackage):
	"""Analysis of COMRADES (Cross-Linking Matched RNA and Deep
Sequencing) Data

	Analysis of RNA crosslinking data for RNA structure prediction. The package is suitable for the analysis of RNA structure cross-linking data and chemical probing data.
	"""
	
	cran = "comradesOO" 

	version("0.1.1", md5="686625ebfc405a2e5ad294c4a3ea4fe1")

	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mixtools", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-r4rna", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-heatmap3", type=("build", "run"))
	depends_on("r-topdom", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-rrna", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
