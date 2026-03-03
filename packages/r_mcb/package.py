# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcb(RPackage):
	"""Model Confidence Bounds

	When choosing proper variable selection methods, it is important to consider the uncertainty of a certain method. The model confidence bound for variable selection identifies two nested models (upper and lower confidence bound models) containing the true model at a given confidence level. A good variable selection method is the one of which the model confidence bound under a certain confidence level has the shortest width. When visualizing the variability of model selection and comparing different model selection procedures, model uncertainty curve is a good graphical tool. A good variable selection method is the one of whose model uncertainty curve will tend to arch towards the upper left corner. This function aims to obtain the model confidence bound and draw the model uncertainty curve of certain single model selection method under a coverage rate equal or little higher than user-given confidential level. About what model confidence bound is and how it work please see Li,Y., Luo,Y., Ferrari,D., Hu,X. and Qin,Y. (2019) Model Confidence Bounds for Variable Selection. Biometrics, 75:392-403. <DOI:10.1111/biom.13024>. Besides, 'flare' is needed only you apply the SQRT or LAD method ('mcb' totally has 8 methods). Although 'flare' has been archived by CRAN, you can still get it in <https://CRAN.R-project.org/package=flare> and the latest version is useful for 'mcb'.
	"""
	
	cran = "mcb" 

	version("0.1.15", md5="d4ec683ce2483e62f446480bbcca90c7")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-leaps", type=("build", "run"))
	depends_on("r-lars", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-ncvreg", type=("build", "run"))
	depends_on("r-smoothmest", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
