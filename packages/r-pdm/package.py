# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdm(RPackage):
	"""Photogrammetric Distances Measurer

	Measures real distances in pictures. With PDM() function, you can choose one '*.jpg' file, select the measure in mm of scale, starting and and finishing point in the graphical scale, the name of the measure, and starting and and finishing point of the measures. After, ask the user for a new measure.
	"""
	
	cran = "PDM" 

	version("0.1", md5="acb5540444a87bf0f96f7fc0aa4da087")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
