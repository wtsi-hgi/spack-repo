# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSgstar(RPackage):
	"""Seasonal Generalized Space Time Autoregressive (S-GSTAR) Model

	A set of function that implements for seasonal multivariate time series analysis based on Seasonal Generalized Space
            Time Autoregressive with Seemingly Unrelated Regression (S-GSTAR-SUR) Model by Setiawan(2016)<https://www.researchgate.net/publication/316517889_S-GSTAR-SUR_model_for_seasonal_spatio_temporal_data_forecasting>.
	"""
	
	homepage = "https://github.com/yogasatria30/sgstar"
	cran = "sgstar" 

	version("0.1.2", md5="40f864e5d1c413971981e669ae8773f4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
