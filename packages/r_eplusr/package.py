# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REplusr(RPackage):
	"""A Toolkit for Using Whole Building Simulation Program
'EnergyPlus'

	A rich toolkit of using the whole building
    simulation program 'EnergyPlus'(<https://energyplus.net>), which
    enables programmatic navigation, modification of 'EnergyPlus' models
    and makes it less painful to do parametric simulations and analysis.
	"""
	
	homepage = "https://hongyuanjia.github.io/eplusr/"
	cran = "eplusr" 

	version("0.16.2", md5="32b360ddcc1ff8f2d5ffcd645680cfa9")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-callr@2.0.4:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-cli@3:", type=("build", "run"))
	depends_on("r-data-table@1.14.6:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-processx@3.2:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("udunits", type=("build", "link", "run"))
