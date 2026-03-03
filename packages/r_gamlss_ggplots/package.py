# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGamlssGgplots(RPackage):
	"""Plotting Functions for Generalized Additive Model for Location
Scale and Shape

	Functions for plotting Generalized Additive Models for Location Scale and Shape from the 'gamlss' package, Stasinopoulos and Rigby (2007) <doi:10.18637/jss.v023.i07>, using the graphical methods from 'ggplot2'.
	"""
	
	homepage = "https://www.gamlss.com/"
	cran = "gamlss.ggplots" 

	version("2.1-12", md5="21350912055a7ef2524a23811aafa887")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gamlss-dist", type=("build", "run"))
	depends_on("r-gamlss@4.3.3:", type=("build", "run"))
	depends_on("r-gamlss-foreach", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
	depends_on("r-gamlss-inf", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-yaimpute", type=("build", "run"))
