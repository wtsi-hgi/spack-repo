# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTandem(RPackage):
	"""A Two-Stage Approach to Maximize Interpretability of Drug
Response Models Based on Multiple Molecular Data Types

	A two-stage regression method that can be used when various input data types are correlated, for example gene expression and methylation in drug response prediction. In the first stage it uses the upstream features (such as methylation) to predict the response variable (such as drug response), and in the second stage it uses the downstream features (such as gene expression) to predict the residuals of the first stage. In our manuscript (Aben et al., 2016, <doi:10.1093/bioinformatics/btw449>), we show that using TANDEM prevents the model from being dominated by gene expression and that the features selected by TANDEM are more interpretable.
	"""
	
	cran = "TANDEM" 

	version("1.0.3", md5="648908c1715c44d4a79a522fe5cc630b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-glmnet@3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
