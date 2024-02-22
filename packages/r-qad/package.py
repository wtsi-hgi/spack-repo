# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQad(RPackage):
	"""Quantification of Asymmetric Dependence

	A copula-based measure for quantifying asymmetry in dependence and associations. Documentation and theory about 'qad' is provided
    by the paper by Junker, Griessenberger & Trutschnig (2021, <doi:10.1016/j.csda.2020.107058>), and the paper by Trutschnig (2011, <doi:10.1016/j.jmaa.2011.06.013>).
	"""
	
	homepage = "https://github.com/griefl/qad"
	cran = "qad" 

	version("1.0.4", md5="3a92eb16ca800df6e30d47e2b8b12b7b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-ggextra", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
