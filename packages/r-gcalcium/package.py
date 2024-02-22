# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGcalcium(RPackage):
	"""A Data Manipulation and Analysis Package for Calcium Indicator
Data

	Provides shortcuts in extracting useful data points and summarizing waveform data. It is optimized for speed to work efficiently with large data sets so you can get to the analysis phase more quickly. It also utilizes a user-friendly format for use by both beginners and seasoned R users.
	"""
	
	cran = "GCalcium" 

	version("1.0.0", md5="999d6d783db54e937edcf635ba754061")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-catools", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
