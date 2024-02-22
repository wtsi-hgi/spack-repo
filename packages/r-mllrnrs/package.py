# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMllrnrs(RPackage):
	"""R6-Based ML Learners for 'mlexperiments'

	Enhances 'mlexperiments'
    <https://CRAN.R-project.org/package=mlexperiments> with additional
    machine learning ('ML') learners. The package provides R6-based
    learners for the following algorithms: 'glmnet'
    <https://CRAN.R-project.org/package=glmnet>, 'ranger'
    <https://CRAN.R-project.org/package=ranger>, 'xgboost'
    <https://CRAN.R-project.org/package=xgboost>, and 'lightgbm'
    <https://CRAN.R-project.org/package=lightgbm>. These can be used
    directly with the 'mlexperiments' R package.
	"""
	
	homepage = "https://github.com/kapsner/mllrnrs"
	cran = "mllrnrs" 

	version("0.0.2", md5="919641c19f22c73ee3b2791558bb5f80")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-kdry", type=("build", "run"))
	depends_on("r-mlexperiments", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
