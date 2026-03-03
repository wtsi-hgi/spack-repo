# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCurtailment(RPackage):
	"""Finds Binary Outcome Designs Using Stochastic Curtailment

	Finds single- and two-arm designs using stochastic curtailment, as described by Law et al. (2022) <doi:10.1080/10543406.2021.2009498> and Law et al. (2021) <doi:10.1002/pst.2067> respectively. Designs can be single-stage or multi-stage. Non-stochastic curtailment is possible as a special case. Desired error-rates, maximum sample size and lower and upper anticipated response rates are inputted and suitable designs are returned with operating characteristics. Stopping boundaries and visualisations are also available. The package can find designs using other approaches, for example designs by Simon (1989) <doi:10.1016/0197-2456(89)90015-9> and Mander and Thompson (2010) <doi:10.1016/j.cct.2010.07.008>. Other features: compare and visualise designs using a weighted sum of expected sample sizes under the null and alternative hypotheses and maximum sample size; visualise any binary outcome design.
	"""
	
	homepage = "https://github.com/martinlaw/curtailment"
	cran = "curtailment" 

	version("0.2.6", md5="be4923383ec1151ab4efeeaa36fefa54")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-pkgcond", type=("build", "run"))
