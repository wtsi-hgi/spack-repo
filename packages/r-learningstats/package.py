# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLearningstats(RPackage):
	"""Elemental Descriptive and Inferential Statistics

	Provides tools to teach students elemental statistics. The main topics covered are descriptive statistics, probability models (discrete and continuous variables) and statistical inference (confidence intervals and hypothesis tests). One of the main advantages of this package is that allows the user to read quite a variety of types of data files with one unique command. Moreover it includes shortcuts to simple but up-to-now not in R descriptive features such a complete frequency table or an histogram with the optimal number of intervals. Related to model distributions (both discrete and continuous), the package allows the student to easy plot the mass/density function, distribution function and quantile function just detailing as input arguments the known population parameters. The inference related tools are basically confidence interval and hypothesis testing. Having defined independent commands for these two tools makes it easier for the student to understand what the software is performing, and it also helps the student to have a better knowledge on which specific tool they need to use in each situation. Moreover, the hypothesis testing commands provide not only the numeric result on the screen but also a very intuitive graph (which includes the statistic distribution, the observed value of the statistic, the rejection area and the p-value) that is very useful for the student to visualise the process. The regression section includes up to now, a simple linear model, with one single command the student can obtain the numeric summary as well as the corresponding diagram with the adjusted regression model and a legend with basic information (formula of the adjusted model and R-squared).
	"""
	
	cran = "LearningStats" 

	version("0.1.0", md5="f9da8b23f9744b06c63cebc117165222")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-readods", type=("build", "run"))
