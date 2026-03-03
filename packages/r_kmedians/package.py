# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKmedians(RPackage):
	"""K-Medians

	Online, Semi-online, and Offline K-medians algorithms are
    given. For both methods, the algorithms can be initialized
    randomly or with the help of a robust hierarchical
    clustering. The number of clusters can be selected with the
    help of a penalized criterion. We provide functions to provide
    robust clustering. Function gen_K() enables to generate a sample
    of data following a contaminated Gaussian mixture.
    Functions Kmedians() and Kmeans() consists in a K-median and a
    K-means algorithms while Kplot() enables to produce graph for both
    methods. 
    Cardot, H., Cenac, P. and Zitt, P-A. (2013). "Efficient and fast estimation of the geometric median in Hilbert spaces with an averaged stochastic gradient algorithm". Bernoulli, 19, 18-43. <doi:10.3150/11-BEJ390>.
    Cardot, H. and Godichon-Baggioni, A. (2017). "Fast Estimation of the Median Covariation Matrix with Application to Online Robust Principal Components Analysis". Test, 26(3), 461-480 <doi:10.1007/s11749-016-0519-x>.
    Godichon-Baggioni, A. and Surendran, S. "A penalized criterion for selecting the number of clusters for K-medians"     <arXiv:2209.03597> 
    Vardi, Y. and Zhang, C.-H. (2000). "The multivariate L1-median and associated data depth". Proc. Natl. Acad. Sci. USA, 97(4):1423-1426. <doi:10.1073/pnas.97.4.1423>.
	"""
	
	cran = "Kmedians" 

	version("2.2.0", md5="14c60204ebf1c6cffa77d1a90ac7f040")

	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-genieclust", type=("build", "run"))
	depends_on("r-gmedian", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-capushe", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
