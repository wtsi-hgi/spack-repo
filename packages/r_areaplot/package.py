# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAreaplot(RPackage):
	"""Plot Stacked Areas and Confidence Bands as Filled Polygons

	Plot stacked areas and confidence bands as filled polygons, or add
  polygons to existing plots. A variety of input formats are supported,
  including vectors, matrices, data frames, formulas, etc.
	"""
	
	homepage = "https://github.com/arni-magnusson/areaplot"
	cran = "areaplot" 

	version("2.1.2", md5="08ce729a7818460af7e696d8f09c631d")

