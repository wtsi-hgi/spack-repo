# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKnitrprogressbar(RPackage):
	"""Provides Progress Bars in 'knitr'

	Provides a progress bar similar to 'dplyr' that can write progress out to a 
    variety of locations, including stdout(), stderr(), or from file(). Useful when using 'knitr' or 'rmarkdown',
    and you still want to see progress of calculations in the terminal.
	"""
	
	homepage = "https://rmflight.github.io/knitrProgressBar"
	cran = "knitrProgressBar" 

	version("1.1.0", md5="3c00371a8fddb9fcc1790fead81b2421")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-r-oo", type=("build", "run"))
