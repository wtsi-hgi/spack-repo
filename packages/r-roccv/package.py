# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoccv(RPackage):
	"""ROC for Cross Validation Results

	Cross validate large genetic data while specifying clinical variables that should always be in the model using the function cv(). An ROC plot from the cross validation data with AUC can be obtained using rocplot(), which also can be used to compare different models. Framework was built to handle genetic data, but works for any data.  
	"""
	
	cran = "roccv" 

	version("1.2", md5="37bb1006da942b04e8c492a41aa02f21")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
