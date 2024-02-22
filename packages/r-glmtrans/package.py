# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmtrans(RPackage):
	"""Transfer Learning under Regularized Generalized Linear Models

	We provide an efficient implementation for two-step multi-source transfer learning algorithms in high-dimensional generalized linear models (GLMs). The elastic-net penalized GLM with three popular families, including linear, logistic and Poisson regression models, can be fitted. To avoid negative transfer, a transferable source detection algorithm is proposed. We also provides visualization for the transferable source detection results. The relevant paper
    is available on arXiv: <arXiv:2105.14328>.
	"""
	
	cran = "glmtrans" 

	version("2.0.0", md5="6ef9ceb5f4affe3ac8cdd53e634c43d4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-formatr", type=("build", "run"))
