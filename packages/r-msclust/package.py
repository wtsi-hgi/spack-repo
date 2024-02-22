# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsclust(RPackage):
	"""Multiple-Scaled Clustering

	Model based clustering using 
    the multivariate multiple Scaled t (MST) and multivariate multiple 
    scaled contaminated normal (MSCN) distributions. The MST is an 
    extension of the multivariate Student-t distribution to include 
    flexible tail behaviors, Forbes, F. & Wraith, D. (2014) <doi:10.1007/s11222-013-9414-4>. The MSCN represents a  heavy-tailed
    generalization of the multivariate normal (MN) distribution to
    model elliptical contoured scatters in the presence of mild outliers
    (also referred to as "bad" points) and automatically detect bad points, Punzo, A. & Tortora, C. (2021) <doi:10.1177/1471082X19890935>.
	"""
	
	cran = "MSclust" 

	version("1.0.3", md5="308bda4dec0457ef0da5ea55df3b67cb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
