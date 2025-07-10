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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/cytofQC_1.2.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/cytofQC/cytofQC_1.2.0.tar.gz"]

	version("1.2.0", sha256="3df2b2baa68bfa6e27c985136842475c458041f11a2a5e831ce99d1c2ebdb087")

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
