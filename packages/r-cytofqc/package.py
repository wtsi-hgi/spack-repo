# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCytofqc(RPackage):
	"""Labels normalized cells for CyTOF data and assigns probabilities for each label

	cytofQC is a package for initial cleaning of CyTOF data. It uses a semi-supervised approach for labeling cells with their most likely data type (bead, doublet, debris, dead) and the probability that they belong to each label type. This package does not remove data from the dataset, but provides labels and information to aid the data user in cleaning their data. Our algorithm is able to distinguish between doublets and large cells.
	"""
	
	homepage = "https://github.com/jillbo1000/cytofQC"
	bioc = "cytofQC"

	version("1.8.0", commit="bd41aa05b90afa0d27e5a6ebe8678d3a70fcf935")
	version("1.2.0", commit="93adeda78b6740a6b539f0bbf128c7814e1755f9")

	depends_on("r-catalyst", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-eztune", type=("build", "run"))
	depends_on("r-gbm", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-hrbrthemes", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-ssc", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
