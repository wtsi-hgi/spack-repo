# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetaneighbor(RPackage):
	"""Single cell replicability analysis

	MetaNeighbor allows users to quantify cell type replicability across datasets using neighbor voting.
	"""
	
	bioc = "MetaNeighbor"

	version("1.28.0", commit="5f7644c73d0ee2c5a2ac603bda2320686e651450")
	version("1.22.0", commit="a036c589ab36fe7966cff8286c86c86d2cae013b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix@1.2:", type=("build", "run"))
	depends_on("r-matrixstats@0.54:", type=("build", "run"))
	depends_on("r-beanplot@1.2:", type=("build", "run"))
	depends_on("r-gplots@3.0.1:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.2:", type=("build", "run"))
	depends_on("r-summarizedexperiment@1.12:", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
