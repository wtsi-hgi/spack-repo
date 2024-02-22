# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPi(RPackage):
	"""Leveraging Genetic Evidence to Prioritise Drug Targets at the Gene and Pathway Level

	Priority index or Pi is developed as a genomic-led target prioritisation system. It integrates functional genomic predictors, knowledge of network connectivity and immune ontologies to prioritise potential drug targets at the gene and pathway level.
	"""
	
	homepage = "http://pi314.r-forge.r-project.org"
	bioc = "Pi" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/Pi_2.14.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/Pi/Pi_2.14.0.tar.gz"]

	version("2.14.0", md5="cb989f0e8a3a1ab90a4a319c860ef602")

	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-suprahex", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggnetwork", type=("build", "run"))
	depends_on("r-osfr", type=("build", "run"))
	depends_on("r-rcircos", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
