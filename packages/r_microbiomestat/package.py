# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicrobiomestat(RPackage):
	"""Statistical Methods for Microbiome Compositional Data

	A suite of methods for powerful and robust microbiome data analysis addressing zero-inflation, phylogenetic structure and compositional effects (Zhou et al. (2022)<doi:10.1186/s13059-022-02655-5>).  The methods can be applied to the analysis of other (high-dimensional) compositional data arising from sequencing experiments.
	"""
	
	cran = "MicrobiomeStat" 

	version("1.2", md5="5af3b2fd4cbb44471678703b43193d84")
	version("1.1", md5="e463de42620bebe5a007bad035b20792")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-modeest", type=("build", "run"))
