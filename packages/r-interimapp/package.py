# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInterimapp(RPackage):
	"""App for Scheduling Interim Analyses in Clinical Trials

	Allows an interactive assessment of the timing of interim analyses. The algorithm simulates both the recruitment and treatment/event phase of a clinical trial based on the package 'interim'.
	"""
	
	cran = "interimApp" 

	version("0.0.1", md5="3805764542eaac22118710b1dc0d190e")

	depends_on("r-interim", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
