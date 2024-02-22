# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlsurvlrnrs(RPackage):
	"""R6-Based ML Survival Learners for 'mlexperiments'

	Enhances 'mlexperiments'
    <https://CRAN.R-project.org/package=mlexperiments> with additional
    machine learning ('ML') learners for survival analysis. The package
    provides R6-based survival learners for the following algorithms:
    'glmnet' <https://CRAN.R-project.org/package=glmnet>, 'ranger'
    <https://CRAN.R-project.org/package=ranger>, 'xgboost'
    <https://CRAN.R-project.org/package=xgboost>, and 'rpart'
    <https://CRAN.R-project.org/package=rpart>. These can be used directly
    with the 'mlexperiments' R package.
	"""
	
	homepage = "https://github.com/kapsner/mlsurvlrnrs"
	cran = "mlsurvlrnrs" 

	version("0.0.2", md5="53b451758a1ac92695aae9de326a82b3")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-kdry", type=("build", "run"))
	depends_on("r-mlexperiments", type=("build", "run"))
	depends_on("r-mllrnrs", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
