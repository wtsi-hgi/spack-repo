# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNlgm(RPackage):
	"""Non Linear Growth Models

	Six growth models are fitted using non-linear least squares. These are the Richards, the 3, 4 and 5 parameter logistic, the Gompetz and the Weibull growth models. Reference: Reddy T., Shkedy Z., van Rensburg C. J., Mwambi H., Debba P., Zuma K. and Manda, S. (2021). "Short-term real-time prediction of total number of reported COVID-19 cases and deaths in South Africa: a data driven approach". BMC medical research methodology, 21(1), 1-11. <doi:10.1186/s12874-020-01165-x>.
	"""
	
	cran = "nlgm" 

	version("1.0", md5="aeb91d0d0631c049a63121801b69409d")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-rfast2", type=("build", "run"))
