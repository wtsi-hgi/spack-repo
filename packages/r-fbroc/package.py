# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFbroc(RPackage):
	"""Fast Algorithms to Bootstrap Receiver Operating Characteristics
Curves

	Implements a very fast C++ algorithm to quickly bootstrap receiver
    operating characteristics (ROC) curves and derived performance metrics,
    including the area under the curve (AUC) and the partial area under the curve as well as 
    the true and false positive rate. The analysis of paired receiver operating curves is supported as well,
    so that a comparison of two predictors is possible. You can also plot the
    results and calculate confidence intervals. On a typical desktop computer the time needed for 
    the calculation of 100000 bootstrap replicates given 500 observations requires time on the
    order of magnitude of one second.
	"""
	
	homepage = "http://www.epeter-stats.de/roc-curve-analysis-with-fbroc/"
	cran = "fbroc" 

	version("0.4.1", md5="c660caa21d9be0c850777a1332db577b")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
