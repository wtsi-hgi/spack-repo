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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/miRLAB_1.32.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/miRLAB/miRLAB_1.32.0.tar.gz"]

	version("1.38.0", tag="RELEASE_3_21")
	version("1.32.0", sha256="85b990ad152ec857d1cfe4ef66cfdacb1248746ed8db9757d3b6e730178930a3")

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
