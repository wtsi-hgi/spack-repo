# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKcprs(RPackage):
	"""Kernel Change Point Detection on the Running Statistics

	The running statistics of interest is first extracted using a time window which is slid across the time series, and in each window, the running statistics value is computed. KCP (Kernel Change Point) detection proposed by Arlot et al. (2012) <arXiv:1202.3878> is then implemented to flag the change points on the running statistics (Cabrieto et al., 2018, <doi:10.1016/j.ins.2018.03.010>). Change points are located by minimizing a variance criterion based on the pairwise similarities between running statistics which are computed via the Gaussian kernel. KCP can locate change points for a given k number of change points. To determine the optimal k, the KCP permutation test is first carried out by comparing the variance of the running statistics extracted from the original data to that of permuted data. If this test is significant, then there is sufficient evidence for at least one change point in the data. Model selection is then used to determine the optimal k>0.
	"""
	
	cran = "kcpRS" 

	version("1.1.1", md5="ae5726f72747db4d42f3b8bcc570ce04")

	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-roll", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
