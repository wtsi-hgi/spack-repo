# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWormtensor(RPackage):
	"""A Clustering Method for Time-Series Whole-Brain Activity Data of
'C. elegans'

	A toolkit to detect clusters from distance matrices. 
    The distance matrices are assumed to be calculated between the cells of 
    multiple animals ('Caenorhabditis elegans') from input time-series matrices. 
    Some functions for generating distance matrices, performing clustering, 
    evaluating the clustering, and visualizing the results of clustering and 
    evaluation are available. We're also providing the download function to 
    retrieve the calculated distance matrices from 
    'figshare' <https://figshare.com>.
	"""
	
	homepage = "https://github.com/rikenbit/WormTensor"
	cran = "WormTensor" 

	version("0.1.0", md5="4d8fa96f27b44b008dc6a603eec74f67")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rtensor", type=("build", "run"))
	depends_on("r-usedist", type=("build", "run"))
	depends_on("r-dtwclust", type=("build", "run"))
	depends_on("r-clustersim", type=("build", "run"))
	depends_on("r-clvalid", type=("build", "run"))
	depends_on("r-aricode", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-uwot", type=("build", "run"))
	depends_on("r-factoextra", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
