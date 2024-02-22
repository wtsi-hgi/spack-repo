# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNca(RPackage):
	"""Necessary Condition Analysis

	Performs a Necessary Condition Analysis (NCA). (Dul, J. 2016. Necessary Condition Analysis (NCA). ''Logic and Methodology of 'Necessary but not Sufficient' causality." Organizational Research Methods 19(1), 10-52) <doi:10.1177/1094428115584005>.
  NCA identifies necessary (but not sufficient) conditions in datasets, where x causes (e.g. precedes) y. Instead of drawing a regression line ''through the middle of the data'' in an xy-plot, NCA draws the ceiling line. The ceiling line y = f(x) separates the area with observations from the area without observations.
  (Nearly) all observations are below the ceiling line: y <= f(x). The empty zone is in the upper left hand corner of the xy-plot (with the convention that the x-axis is ''horizontal'' and the y-axis is ''vertical'' and that values increase ''upwards'' and ''to the right''). The ceiling line is a (piecewise) linear non-decreasing line: a linear step function or a straight line. It indicates which level of x (e.g. an effort or input) is necessary but not sufficient for a (desired) level of y (e.g. good performance or output). A quick start guide for using this package can be found here: <https://repub.eur.nl/pub/78323/> or <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2624981>.
	"""
	
	homepage = "https://www.erim.eur.nl/necessary-condition-analysis/"
	cran = "NCA" 

	version("4.0.0", md5="5d07ee38c1046042d124859b0a02f0c4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
