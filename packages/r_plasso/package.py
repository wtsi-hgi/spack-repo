# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlasso(RPackage):
	"""Cross-Validated (Post-) Lasso

	Built on top of the 'glmnet' library by Friedman, Hastie and Tibshirani (2010) <doi:10.18637/jss.v033.i01>, the 'plasso' package follows Knaus (2022) <doi:10.1093/ectj/utac015> and comes up with two functions that estimate least squares Lasso and Post-Lasso models.
  The plasso() function adds coefficient paths for a Post-Lasso model to the standard 'glmnet' output.
  On top of that cv.plasso() cross-validates the coefficient paths for both the Lasso and Post-Lasso model and provides optimal hyperparameter values for the penalty term lambda.
	"""
	
	homepage = "https://github.com/stefan-1997/plasso"
	cran = "plasso" 

	version("0.1.2", md5="8dc580ab11e2f9330ba755efba80a43b")

	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
