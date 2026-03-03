# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetaanalyser(RPackage):
	"""An Interactive Visualisation of Meta-Analysis as a Physical
Weighing Machine

	An interactive application to visualise meta-analysis data as a
    physical weighing machine. The interface is based on the Shiny web application
    framework, though can be run locally and with the user's own data.
	"""
	
	homepage = "https://github.com/chjackson/MetaAnalyser"
	cran = "MetaAnalyser" 

	version("0.2.1", md5="36af9692634b452347daa5f3d47b291c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-ggvis", type=("build", "run"))
	depends_on("r-dt@0.1.40:", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
