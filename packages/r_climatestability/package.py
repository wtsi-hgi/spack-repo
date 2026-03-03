# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClimatestability(RPackage):
	"""Estimating Climate Stability from Climate Model Data

	Climate stability measures are not formalized in the literature and
  tools for generating stability metrics from existing data are nascent.
  This package provides tools for calculating climate stability from raster data
  encapsulating climate change as a series of time slices. The methods follow
  Owens and Guralnick <doi:10.17161/bi.v14i0.9786> Biodiversity Informatics.
	"""
	
	homepage = "https://github.com/hannahlowens/climateStability"
	cran = "climateStability" 

	version("0.1.4", md5="b5fc7219bd271f7f203fd0c8b41c66dc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
