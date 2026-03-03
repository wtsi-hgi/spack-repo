# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCompetitiontoolbox(RPackage):
	"""A Graphical User Interface for Antitrust and Trade Practitioners

	A graphical user interface for simulating the effects of mergers, tariffs, and quotas under an
             assortment of different economic models. The interface is powered by the 'Shiny' web application framework from 
             'RStudio'.
	"""
	
	homepage = "https://github.com/luciu5/competitiontoolbox"
	cran = "competitiontoolbox" 

	version("0.7.1", md5="ee31e39d5e0a5a006f33a21dd96ee317")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-antitrust@0.99.11:", type=("build", "run"))
	depends_on("r-trade@0.5.4:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rhandsontable", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
