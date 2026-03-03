# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModelcharts(RPackage):
	"""Classification Model Charts

	Provides two important functions for producing Gain chart and Lift chart for any classification model.
	"""
	
	cran = "Modelcharts" 

	version("0.1.0", md5="6f7e07915ab760c0df8b19142fec2506")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
