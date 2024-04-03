# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrSc(RPackage):
	"""Joint Dimension Reduction and Spatial Clustering

	Joint dimension reduction and spatial clustering is conducted for
    Single-cell RNA sequencing and spatial transcriptomics data, and more details can be referred to 
    Wei Liu, Xu Liao, Yi Yang, Huazhen Lin, Joe Yeong, Xiang Zhou, Xingjie Shi and Jin Liu. (2022) <doi:10.1093/nar/gkac219>. It is not only computationally efficient and scalable to the sample size increment, but also is capable of choosing the smoothness parameter and the number of clusters as well.
	"""
	
	homepage = "https://github.com/feiyoung/DR.SC"
	cran = "DR.SC" 

	version("3.3", md5="81d75c7f73563257ec57c1de9bacc03d")
	version("3.4", md5="f194e3a62f05b629ee1dd28a1ede6fc9")

	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r@4:", type=("build", "run"))
	depends_on("r-compquadform", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-giraf", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
