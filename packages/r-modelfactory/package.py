# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModelfactory(RPackage):
	"""Combine Statistical Models into a Tibble for Comparison

	Statisticians often want to compare the fit of different models on 
    the same data set. However, this usually involves a lot of manual code to 
    fish items out of summary() or plain model objects. 'modelfactory' offers 
    the capability to pass multiple models in and get out metrics or 
    coefficients for quick comparison with easy-to-remember syntax.
	"""
	
	homepage = "https://willtirone.github.io/modelfactory/"
	cran = "modelfactory" 

	version("1.0.0", md5="72e84a995aeb3950cd827e7eb2507e08")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
