# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RC060(RPackage):
	"""Extended Inference for Lasso and Elastic-Net Regularized Cox and
Generalized Linear Models

	The c060 package provides additional functions to perform stability selection, model validation and parameter tuning for glmnet models.
	"""
	
	homepage = "https://github.com/fbertran/c060/"
	cran = "c060" 

	version("0.3-0", md5="e2d0ae87e4a1229772b0c56eb09d0bda", url="https://cran.r-project.org/src/contrib/c060_0.3-0.tar.gz")

	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mlegp", type=("build", "run"))
	depends_on("r-tgp", type=("build", "run"))
	depends_on("r-peperr", type=("build", "run"))
	depends_on("r-penalized", type=("build", "run"))
	depends_on("r-penalizedsvm", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
