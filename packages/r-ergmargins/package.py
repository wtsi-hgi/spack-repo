# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RErgmargins(RPackage):
	"""Process Analysis for Exponential Random Graph Models

	Calculates marginal effects and conducts process analysis in exponential family random graph models (ERGM).
    Includes functions to conduct mediation and moderation analyses and to diagnose
    multicollinearity.
    URL: <https://github.com/sduxbury/ergMargins>.
    BugReports: <https://github.com/sduxbury/ergMargins/issues>.
    Duxbury, Scott W (2021) <doi:10.1177/0049124120986178>.
    Long, J. Scott, and Sarah Mustillo (2018) <doi:10.1177/0049124118799374>.
    Mize, Trenton D. (2019) <doi:10.15195/v6.a4>.
    Karlson, Kristian Bernt, Anders Holm, and Richard Breen (2012) <doi:10.1177/0081175012444861>.
    Duxbury, Scott W (2018) <doi:10.1177/0049124118782543>.
    Duxbury, Scott W, Jenna Wertsching (2023) <doi:10.1016/j.socnet.2023.02.003>.
    Huang, Peng, Carter Butts (2023) <doi:10.1016/j.socnet.2023.07.001>.
	"""
	
	cran = "ergMargins" 

	version("1.1", md5="54b0885ad2ee51677ad282db1604c633")

	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-ergm", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-btergm", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-sna", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-sampling", type=("build", "run"))
