# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIpcaps(RPackage):
	"""Iterative Pruning to Capture Population Structure

	An unsupervised clustering algorithm based on iterative pruning is for capturing population structure. This version supports ordinal data which can be applied directly to SNP data to identify fine-level population structure and it is built on the iterative pruning Principal Component Analysis ('ipPCA') algorithm as explained in Intarapanich et al. (2009) <doi:10.1186/1471-2105-10-382>. The 'IPCAPS' involves an iterative process using multiple splits based on multivariate Gaussian mixture modeling of principal components and 'Expectation-Maximization' clustering as explained in Lebret et al. (2015) <doi:10.18637/jss.v067.i06>. In each iteration, rough clusters and outliers are also identified using the function rubikclust() from the R package 'KRIS'.
	"""
	
	homepage = "https://gitlab.com/kris.ccp/ipcaps"
	cran = "IPCAPS" 

	version("1.1.8", md5="f10ab496e14bc93dbd37dd10eef71ec2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-kris", type=("build", "run"))
	depends_on("r-fpc", type=("build", "run"))
	depends_on("r-lpcm", type=("build", "run"))
	depends_on("r-apcluster", type=("build", "run"))
	depends_on("r-rmixmod", type=("build", "run"))
