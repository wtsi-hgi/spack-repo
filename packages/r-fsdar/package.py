# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFsdar(RPackage):
	"""Robust Data Analysis Through Monitoring and Dynamic
Visualization

	Provides interface to the 'MATLAB' toolbox 'Flexible Statistical Data Analysis
    (FSDA)' which is comprehensive and computationally efficient
    software package for robust statistics in regression, multivariate
    and categorical data analysis. The current R version implements tools
    for regression: (forward search, S- and MM-estimation, least trimmed
    squares (LTS) and least median of squares (LMS)), for multivariate analysis
    (forward search, S- and MM-estimation), for cluster analysis and cluster-wise regression.
    The distinctive feature of our package is the possibility of
    monitoring the statistics of interest as a function of breakdown point,
    efficiency or subset size, depending on the estimator. This is
    accompanied by a rich set of graphical features, such as dynamic
    brushing, linking, particularly useful for exploratory data analysis.
	"""
	
	homepage = "https://github.com/UniprJRC/fsdaR"
	cran = "fsdaR" 

	version("0.9-0", md5="3b2a1e4ddd2b6c73fdf3e480525723b2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("matlab", type=("build", "link", "run"))
	depends_on("openjdk@1.8:", type=("build", "link", "run"))
