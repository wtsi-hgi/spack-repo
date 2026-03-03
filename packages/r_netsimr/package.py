# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetsimr(RPackage):
	"""Actuarial Functions for Non-Life Insurance Modelling

	Assists actuaries and other insurance modellers in pricing,
    reserving and capital modelling for non-life insurance and
    reinsurance modelling. Provides functions that help model
    excess levels, capping and pure Incurred but not reported
    claims (pure IBNR).
    Includes capped mean, exposure curves and increased limit
    factor curves (ILFs) for LogNormal, Gamma, Pareto, Sliced
    LogNormal-Pareto and Sliced Gamma-Pareto distributions.
    Includes mean, probability density function (pdf), cumulative
    probability function (cdf) and inverse cumulative probability
    function for Sliced LogNormal-Pareto and Sliced Gamma-Pareto
    distributions.
    Includes calculating pure IBNR exposure with LogNormal and
    Gamma distribution for reporting delay.
    Includes three shiny tools, one to simulate insurance claims applying
    reinsurance structures, fit generalised linear models and fit claims
    frequency or severity distributions.
    Methods used in the package refer to
    Free for All by Yiannis Parizas (2023) <https://www.theactuary.com/2023/03/02/free-all>;
    Escaping the triangle by Yiannis Parizas (2019) <https://www.theactuary.com/features/2019/06/2019/06/05/escaping-triangle>;
    Take to excess by Yiannis Parizas (2019) <https://www.theactuary.com/features/2019/03/2019/03/06/taken-excess>.
	"""
	
	cran = "NetSimR" 

	version("0.1.5", md5="bfd54a4c9863f3ae844ea6c4d80c1cbb")

	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinybusy", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rmysql", type=("build", "run"))
	depends_on("r-rodbc", type=("build", "run"))
	depends_on("r-rpostgresql", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-pareto", type=("build", "run"))
