# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWppi(RPackage):
	"""Weighting protein-protein interactions

	Protein-protein interaction data is essential for omics data analysis and modeling. Database knowledge is general, not specific for cell type, physiological condition or any other context determining which connections are functional and contribute to the signaling. Functional annotations such as Gene Ontology and Human Phenotype Ontology might help to evaluate the relevance of interactions. This package predicts functional relevance of protein-protein interactions based on functional annotations such as Human Protein Ontology and Gene Ontology, and prioritizes genes based on network topology, functional scores and a path search algorithm.
	"""
	
	homepage = "https://github.com/AnaGalhoz37/wppi"
	bioc = "wppi" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/wppi_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/wppi/wppi_1.10.0.tar.gz"]

	version("1.16.0", tag="RELEASE_3_21")
	version("1.10.0", sha256="4bd8bb3374f1b25ef727e0cc5d3bae4d84ca297ee0bc3d70459c3fc00a318f13")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-logger", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-omnipathr@2.99.8:", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
