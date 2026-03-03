# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChangepoint(RPackage):
	"""Methods for Changepoint Detection

	Implements various mainstream and specialised changepoint methods for finding single and multiple changepoints within data.  Many popular non-parametric and frequentist methods are included.  The cpt.mean(), cpt.var(), cpt.meanvar() functions should be your first point of call.
	"""
	
	homepage = "https://github.com/rkillick/changepoint/"
	cran = "changepoint" 

	version("2.2.4", md5="e1d6ec86180eeeaf36c3de1f54c872a0")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-zoo@0.9.1:", type=("build", "run"))
