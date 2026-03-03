# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuadratik(RPackage):
	"""Collection of Methods Constructed using Kernel-Based Quadratic
Distances

	It includes test for multivariate normality, test for uniformity on the Sphere, non-parametric two- and k-sample tests, random generation of points from the Poisson kernel-based density and clustering algorithm for spherical data. For more information see Saraceno, G., Markatou, M., Mukhopadhyay, R., Golzy, M. (2024) <arxiv:2402.02290>, 
    Ding, Y., Markatou, M., Saraceno, G. (2023) <doi:10.5705/ss.202022.0347>, and 
    Golzy, M., Markatou, M. (2020) <doi:10.1080/10618600.2020.1740713>.
	"""
	
	cran = "QuadratiK" 

	version("1.0.0", md5="53007924e6e2a4026c63e1ef2646c253")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-sn", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-movmf", type=("build", "run"))
	depends_on("r-rlecuyer", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-tinflex", type=("build", "run"))
	depends_on("r-ggpp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-clusterrepro", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-rrcov", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
