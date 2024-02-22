# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCosinor(RPackage):
	"""Tools for Estimating and Predicting the Cosinor Model

	A set of simple functions that transforms longitudinal
    data to estimate the cosinor linear model as described in Tong (1976).
    Methods are given to summarize the mean, amplitude and acrophase, to
    predict the mean annual outcome value, and to test the coefficients.
	"""
	
	homepage = "https://github.com/sachsmc/cosinor"
	cran = "cosinor" 

	version("1.2.3", md5="00b6dcc09a53ae4e4294a538c624b10a")

	depends_on("r@2.11:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
