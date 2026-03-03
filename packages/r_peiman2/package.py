# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPeiman2(RPackage):
	"""Post-Translational Modification Enrichment, Integration, and
Matching Analysis

	Functions and mined database from 'UniProt' focusing on post-translational modifications to do single enrichment analysis (SEA) and protein set enrichment analysis (PSEA). Payman Nickchi, Mehdi Mirzaie, Marc Baumann, Amir Ata Saei, Mohieddin Jafari (2022) <bioRxiv:10.1101/2022.11.09.515610>.
	"""
	
	cran = "PEIMAN2" 

	version("0.1.0", md5="52425685c92742789b36e0eb954a1360", url="https://cran.r-project.org/src/contrib/PEIMAN2_0.1.0.tar.gz")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
