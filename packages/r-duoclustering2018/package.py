# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDuoclustering2018(RPackage):
	"""Data, Clustering Results and Visualization Functions From Duò et al (2018)

	Preprocessed experimental and simulated scRNA-seq data sets used for evaluation of clustering methods for scRNA-seq data in Duò et al (2018). Also contains results from applying several clustering methods to each of the data sets, and functions for plotting method performance.
	"""
	
	bioc = "DuoClustering2018" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/DuoClustering2018_1.20.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/DuoClustering2018/DuoClustering2018_1.20.0.tar.gz"]

	version("1.20.0", md5="a2761f4db56025af2eaf8240392d01a0", url="https://www.bioconductor.org/packages/release/data/experiment/src/contrib/DuoClustering2018_1.20.0.tar.gz")

	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))

	# experiment