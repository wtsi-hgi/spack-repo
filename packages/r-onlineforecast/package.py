# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROnlineforecast(RPackage):
	"""Forecast Modelling for Online Applications

	A framework for fitting adaptive forecasting models. Provides a way to use forecasts as input to models, e.g. weather forecasts for energy related forecasting. The models can be fitted recursively and can easily be setup for updating parameters when new data arrives. See the included vignettes, the website <https://onlineforecasting.org> and the paper "onlineforecast: An R package for adaptive and recursive forecasting" <https://journal.r-project.org/articles/RJ-2023-031/>.
	"""
	
	homepage = "https://onlineforecasting.org"
	cran = "onlineforecast" 

	version("1.0.2", md5="cca46ada072aba0ad1b4fedf2e6573ba")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-r6@2.2.2:", type=("build", "run"))
	depends_on("r-pbs", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
