# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMirlab(RPackage):
	"""Dry lab for exploring miRNA-mRNA relationships

	Provide tools exploring miRNA-mRNA relationships, including popular miRNA target prediction methods, ensemble methods that integrate individual methods, functions to get data from online resources, functions to validate the results, and functions to conduct enrichment analyses.
	"""
	
	homepage = "https://github.com/pvvhoang/miRLAB"
	bioc = "miRLAB"

	version("1.38.0", commit="d0c410404bb8859c64f9a15e824c5830540c9baa")
	version("1.32.0", commit="10514c47d81e45d309b5ba96e5815ed066f953bf")

	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-energy", type=("build", "run"))
	depends_on("r-entropy", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-pcalg", type=("build", "run"))
	depends_on("r-tcgabiolinks", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-ctc", type=("build", "run"))
	depends_on("r-invariantcausalprediction", type=("build", "run"))
	depends_on("r-category", type=("build", "run"))
	depends_on("r-gostats", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
