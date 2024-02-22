# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClusroc(RPackage):
	"""ROC Analysis in Three-Class Classification Problems for
Clustered Data

	Statistical methods for ROC surface analysis in three-class classification problems for clustered data and in presence of covariates. In particular, the package allows to obtain covariate-specific point and interval estimation for:
  (i) true class fractions (TCFs) at fixed pairs of thresholds;
  (ii) the ROC surface;
  (iii) the volume under ROC surface (VUS);
  (iv) the optimal pairs of thresholds.
  Methods considered in points (i), (ii) and (iv) are proposed and discussed in To et al. (2022) <doi:10.1177/09622802221089029>. Referring to point (iv), three  different selection criteria are implemented: Generalized Youden Index (GYI), Closest to Perfection (CtP) and Maximum Volume (MV). Methods considered in point (iii) are proposed and discussed in Xiong et al. (2018) <doi:10.1177/0962280217742539>. Visualization tools are also provided. We refer readers to the articles cited above for all details. 
	"""
	
	homepage = "https://github.com/toduckhanh/ClusROC"
	cran = "ClusROC" 

	version("1.0.2", md5="a7296f616920ace606f430223ecfe26f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
