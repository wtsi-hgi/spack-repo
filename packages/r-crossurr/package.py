# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrossurr(RPackage):
	"""Cross-Fitting for Doubly Robust Evaluation of High-Dimensional
Surrogate Markers

	Doubly robust methods for evaluating surrogate markers as outlined in: Agniel D, Hejblum BP, Thiebaut R & Parast L (2022). 
             "Doubly robust evaluation of high-dimensional surrogate markers", Biostatistics <doi:10.1093/biostatistics/kxac020>. You can use these methods to determine how much of the overall treatment effect is explained by a (possibly high-dimensional) set of surrogate markers.
	"""
	
	cran = "crossurr" 

	version("1.0.6", md5="b2d195b8ce6d9433cb24ace71bb8d636")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gbm", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-rcal", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sis", type=("build", "run"))
	depends_on("r-superlearner", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
