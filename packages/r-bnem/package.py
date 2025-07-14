# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBnem(RPackage):
	"""Training of logical models from indirect measurements of perturbation experiments

	bnem combines the use of indirect measurements of Nested Effects Models (package mnem) with the Boolean networks of CellNOptR. Perturbation experiments of signalling nodes in cells are analysed for their effect on the global gene expression profile. Those profiles give evidence for the Boolean regulation of down-stream nodes in the network, e.g., whether two parents activate their child independently (OR-gate) or jointly (AND-gate).
	"""
	
	homepage = "https://github.com/MartinFXP/bnem/"
	bioc = "bnem" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/bnem_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/bnem/bnem_1.10.0.tar.gz"]

	version("1.16.0", tag="RELEASE_3_21")
	version("1.10.0", sha256="ba3014cf2a72af41a66cc61a1cb35c7b755bf3c69205d866b0258cd697c98572")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-cellnoptr", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-snowfall", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-flexclust", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-epinem", type=("build", "run"))
	depends_on("r-mnem", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-binom", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-sva", type=("build", "run"))
	depends_on("r-vsn", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
