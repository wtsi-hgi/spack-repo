# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTeal(RPackage):
	"""Exploratory Web Apps for Analyzing Clinical Trials Data

	A 'shiny' based interactive exploration framework for
    analyzing clinical trials data. 'teal' currently provides a dynamic
    filtering facility and different data viewers. 'teal' 'shiny'
    applications are built using standard 'shiny' modules.
	"""
	
	homepage = "https://insightsengineering.github.io/teal/"
	cran = "teal" 

	version("0.15.2", md5="2937842bbfac5fdabd0be67851990cfa")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-shiny@1.7:", type=("build", "run"))
	depends_on("r-teal-data@0.4:", type=("build", "run"))
	depends_on("r-teal-slice@0.5:", type=("build", "run"))
	depends_on("r-checkmate@2.1:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lifecycle@0.2:", type=("build", "run"))
	depends_on("r-logger@0.2:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-teal-code@0.5:", type=("build", "run"))
	depends_on("r-teal-logger@0.1.1:", type=("build", "run"))
	depends_on("r-teal-reporter@0.2:", type=("build", "run"))
	depends_on("r-teal-widgets@0.4:", type=("build", "run"))
