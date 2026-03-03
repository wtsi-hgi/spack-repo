# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnsemblemos(RPackage):
	"""Ensemble Model Output Statistics

	Ensemble Model Output Statistics to create probabilistic
        forecasts from ensemble forecasts and weather observations.
	"""
	
	cran = "ensembleMOS" 

	version("0.8.2", md5="7bf6a58c82516bbd399659828641f742")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ensemblebma", type=("build", "run"))
	depends_on("r-chron", type=("build", "run"))
	depends_on("r-evd", type=("build", "run"))
