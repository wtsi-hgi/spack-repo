# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmcorr(RPackage):
	"""Repeated Measures Correlation

	Compute the repeated measures correlation, a statistical technique
    for determining the overall within-individual relationship among paired measures
    assessed on two or more occasions, first introduced by Bland and Altman (1995).
    Includes functions for diagnostics, p-value, effect size with confidence
    interval including optional bootstrapping, as well as graphing. Also includes
    several example datasets. For more details, see the web documentation 
    <https://lmarusich.github.io/rmcorr/index.html> and the 
    original paper: Bakdash and Marusich (2017) <doi:10.3389/fpsyg.2017.00456>.
	"""
	
	homepage = "https://github.com/lmarusich/rmcorr"
	cran = "rmcorr" 

	version("0.6.0", md5="6910a66ee2d82bbf2126a22527d6adbc")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
