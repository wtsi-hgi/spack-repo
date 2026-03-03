# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParmsurvfit(RPackage):
	"""Parametric Models for Survival Data

	Executes simple parametric models for right-censored 
    survival data.  Functionality emulates capabilities in 'Minitab', including
    fitting right-censored data, assessing fit, plotting survival functions,
    and summary statistics and probabilities.
	"""
	
	homepage = "https://github.com/apjacobson/parmsurvfit"
	cran = "parmsurvfit" 

	version("0.1.0", md5="a2e47f8c275762af20af39ed1c32affc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-flexsurv", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
