# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMovieroc(RPackage):
	"""Visualizing the Decision Rules Underlying Binary Classification

	Visualization of decision rules for binary classification and Receiver Operating Characteristic (ROC) curve estimation under different generalizations:
  - making the classification subsets flexible to cover those scenarios where both extremes of the
  marker are associated with a higher risk of being positive, considering two thresholds 
  (gROC curve);
  - transforming the marker by a function either defined by the user or resulting from a logistic 
  regression model (hROC curve);
  - considering a linear transformation with some fixed parameters introduced by the user, 
  dynamic parameters or empirically maximizing TPR for each FPR for a bivariate marker.
  Also a quadratic transformation with particular coefficients or a function fitted by a logistic 
  regression model can be considered (biROC curve);
  - considering a linear transformation with some fixed parameters introduced by the user, 
  dynamic parameters or a function fitted by a logistic regression model (multiROC curve).
  The classification regions behind each point of the ROC curve are displayed in both fixed 
  graphics (plot.buildROC(), plot.regions() or plot.funregions() function) or videos (movieROC() 
  function).
	"""
	
	cran = "movieROC" 

	version("0.1.0", md5="1b9c94f51c2a4f00c572b7ec44ccf1c6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
	depends_on("r-animation", type=("build", "run"))
	depends_on("r-intrval", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
