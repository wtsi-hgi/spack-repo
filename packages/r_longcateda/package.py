# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLongcateda(RPackage):
	"""Package for Plotting Categorical Longitudinal and Time-Series
Data

	Methods for plotting categorical longitudinal and time-series data by mapping individuals to the vertical space (each horizontal line represents a participant), time (or repeated measures) to the horizontal space, categorical (or discrete) states as facets using color or shade, and events to points using plotting characters. Sorting individuals in the vertical space and (or) stratifying them by groups can reveal patterns in the changes over time.
	"""
	
	cran = "longCatEDA" 

	version("0.31", md5="73427449976bdd3c22dfbf26d0f7e4a7")

