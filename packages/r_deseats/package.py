# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeseats(RPackage):
	"""Data-Driven Locally Weighted Regression for Trend and
Seasonality in TS

	Various methods for the identification of trend and seasonal
  components in time series (TS) are provided. Among them is a data-driven locally
  weighted regression approach with automatically selected bandwidth for
  equidistant short-memory time series. The approach is a
  combination / extension of the algorithms by
  Feng (2013) <doi:10.1080/02664763.2012.740626> and Feng, Y., Gries, T.,
  and Fritz, M. (2020) <doi:10.1080/10485252.2020.1759598> and a brief
  description of this new method is provided in the package documentation.
  Furthermore, the package allows its users to apply the base model of the
  Berlin procedure, version 4.1, as described in Speth (2004) <https://www.destatis.de/DE/Methoden/Saisonbereinigung/BV41-methodenbericht-Heft3_2004.pdf?__blob=publicationFile>.
  Permission to include this procedure was kindly provided by the Federal
  Statistical Office of Germany.
	"""
	
	cran = "deseats" 

	version("1.0.0", md5="ec66685481fad8088178439b122df8e1")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-animation", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
