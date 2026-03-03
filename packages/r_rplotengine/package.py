# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRplotengine(RPackage):
	"""R as a Plotting Engine

	Generate basic charts either by custom applications, or from a small script launched from the system console, or within the R console. Two ASCII text files are necessary:
  (1) The graph parameters file, which name is passed to the function 'rplotengine()'.
      The user can specify the titles, choose the type of the graph, graph output formats
      (e.g. png, eps), proportion of the X-axis and Y-axis, position of the legend,
      whether to show or not a grid at the background, etc.
  (2) The data to be plotted, which name is specified as a parameter ('data_filename')
      in the previous file. This data file has a tabulated format, with a single character
      (e.g. tab) between each column. Optionally, the file could include data columns for
      showing confidence intervals.
	"""
	
	homepage = "http://www.umh.es"
	cran = "rplotengine" 

	version("1.0-9", md5="58198ab80a8dc0b09ecd2c4e414b5ecf")

	depends_on("r@2.6.2:", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
