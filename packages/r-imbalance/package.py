# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImbalance(RPackage):
	"""Preprocessing Algorithms for Imbalanced Datasets

	Class imbalance usually damages the performance of classifiers. Thus, it is
             important to treat data before applying a classifier algorithm. This package
             includes recent resampling algorithms in the literature: (Barua et al. 2014)
             <doi:10.1109/tkde.2012.232>; (Das et al. 2015) <doi:10.1109/tkde.2014.2324567>,
             (Zhang et al. 2014) <doi:10.1016/j.inffus.2013.12.003>; (Gao et al. 2014)
             <doi:10.1016/j.neucom.2014.02.006>; (Almogahed et al. 2014)
             <doi:10.1007/s00500-014-1484-5>. It also includes an useful interface to
             perform oversampling.
	"""
	
	homepage = "http://github.com/ncordon/imbalance"
	cran = "imbalance" 

	version("1.0.2.1", md5="5dc043a5c75be6032f3cd6d195d8f316")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-bnlearn", type=("build", "run"))
	depends_on("r-kernelknn", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-smotefamily", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-c50", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
