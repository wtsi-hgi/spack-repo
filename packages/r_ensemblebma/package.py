# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnsemblebma(RPackage):
	"""Probabilistic Forecasting using Ensembles and Bayesian Model
Averaging

	Bayesian Model Averaging to create probabilistic forecasts
        from ensemble forecasts and weather observations
 <https://stat.uw.edu/sites/default/files/files/reports/2007/tr516.pdf>.
	"""
	
	cran = "ensembleBMA" 

	version("5.1.8", md5="c2b465c0a5ecf877245c784abff0da4e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-chron", type=("build", "run"))
