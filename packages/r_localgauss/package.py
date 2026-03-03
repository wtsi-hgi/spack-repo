# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLocalgauss(RPackage):
	"""Estimating Local Gaussian Parameters

	Computational routines for estimating local Gaussian parameters. Local Gaussian parameters are useful for characterizing and testing for non-linear dependence within bivariate data. See e.g. Tjostheim and Hufthammer, Local Gaussian correlation: A new measure of dependence, Journal of Econometrics, 2013, Volume 172 (1), pages 33-48 <DOI:10.1016/j.jeconom.2012.08.001>.
	"""
	
	cran = "localgauss" 

	version("0.41", md5="fa749c110e378c8f81f53e5a7e99c925")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
