# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrthos(RPackage):
	"""`orthos` is an R package for variance decomposition using conditional variational auto-encoders

	`orthos` decomposes RNA-seq contrasts, for example obtained from a gene knock-out or compound treatment experiment, into unspecific and experiment-specific components. Original and decomposed contrasts can be efficiently queried against a large database of contrasts (derived from ARCHS4, https://maayanlab.cloud/archs4/) to identify similar experiments. `orthos` furthermore provides plotting functions to visualize the results of such a search for similar contrasts.
	"""
	
	bioc = "orthos" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/orthos_1.0.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/orthos/orthos_1.0.1.tar.gz"]

	version("1.0.1", sha256="8b7b30496fe70f7dd55c55a87894b01003cc1628100ed0de5f8b71bdaaa62b6a")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-basilisk", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-ggsci", type=("build", "run"))
	depends_on("r-hdf5array", type=("build", "run"))
	depends_on("r-keras", type=("build", "run"))
	depends_on("r-orthosdata", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-tensorflow", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
