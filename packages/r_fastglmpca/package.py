# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastglmpca(RPackage):
	"""Fast Algorithms for Generalized Principal Component Analysis

	Implements fast, scalable optimization algorithms for
    fitting generalized principal components analysis (GLM-PCA) models,
    as described in "A Generalization of Principal Components
    Analysis to the Exponential Family" Collins M, Dasgupta S, Schapire RE
    (2002, ISBN:9780262271738), and subsequently "Feature Selection 
    and Dimension Reduction for Single-Cell RNA-Seq Based on a Multinomial
    Model" Townes FW, Hicks SC, Aryee MJ, Irizarry RA (2019)
    <doi:10.1186/s13059-019-1861-6>.
	"""
	
	homepage = "https://github.com/stephenslab/fastglmpca"
	cran = "fastglmpca" 

	version("0.1-103", md5="0247b27edece1528dfd87cf4a53e2dc5")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixextra", type=("build", "run"))
	depends_on("r-distr", type=("build", "run"))
	depends_on("r-daarem", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
