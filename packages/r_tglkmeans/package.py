# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTglkmeans(RPackage):
	"""Efficient Implementation of K-Means++ Algorithm

	Efficient implementation of K-Means++ algorithm. For more
    information see (1) "kmeans++ the advantages of the k-means++
    algorithm" by David Arthur and Sergei Vassilvitskii (2007),
    Proceedings of the eighteenth annual ACM-SIAM symposium on Discrete
    algorithms, Society for Industrial and Applied Mathematics,
    Philadelphia, PA, USA, pp. 1027-1035, and (2) "The Effectiveness of
    Lloyd-Type Methods for the k-Means Problem" by Rafail Ostrovsky, Yuval
    Rabani, Leonard J. Schulman and Chaitanya Swamy
    <doi:10.1145/2395116.2395117>.
	"""
	
	homepage = "https://tanaylab.github.io/tglkmeans/"
	cran = "tglkmeans" 

	version("0.5.4", md5="a138e0800e6d26be7b6d6fed25efa667")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dofuture", type=("build", "run"))
	depends_on("r-dplyr@0.5:", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-ggplot2@2.2:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-plyr@1.8.4:", type=("build", "run"))
	depends_on("r-purrr@0.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-tgstat@1:", type=("build", "run"))
	depends_on("r-tibble@3.1.2:", type=("build", "run"))
