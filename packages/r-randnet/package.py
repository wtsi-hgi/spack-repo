# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRandnet(RPackage):
	"""Random Network Model Estimation, Selection and Parameter Tuning

	Model selection and parameter tuning procedures for a class of random network models. The model selection can be done by a general cross-validation framework called ECV from Li et. al. (2016) <arXiv:1612.04717> . Several other model-based and task-specific methods are also included, such as NCV from Chen and Lei (2016) <arXiv:1411.1715>, likelihood ratio method from Wang and Bickel (2015) <arXiv:1502.02069>, spectral methods from Le and Levina (2015) <arXiv:1507.00827>. Many network analysis methods are also implemented, such as the regularized spectral clustering (Amini et. al. 2013 <doi:10.1214/13-AOS1138>) and its degree corrected version and graphon neighborhood smoothing (Zhang et. al. 2015 <arXiv:1509.08588>). It also includes the consensus clustering of Gao et. al. (2014) <arXiv:1410.5837>, the method of moments estimation of nomination SBM of Li et. al. (2020) <arxiv:2008.03652>, and the network mixing method of Li and Le (2021) <arxiv:2106.02803>. It also includes the informative core-periphery data processing method of Miao and Li (2021) <arXiv:2101.06388>. The work to build and improve this package is partially supported by the NSF grants DMS-2015298 and DMS-2015134.
	"""
	
	cran = "randnet" 

	version("0.7", md5="343117cae7490c18ffce34478ac5083f")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-entropy", type=("build", "run"))
	depends_on("r-auc", type=("build", "run"))
	depends_on("r-sparseflmm", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-powerlaw", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-nnls", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
