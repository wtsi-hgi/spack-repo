# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeas(RPackage):
	"""Seasonal Analysis and Graphics, Especially for Climatology

	Capable of deriving seasonal statistics, such as "normals", and
  analysis of seasonal data, such as departures. This package also has
  graphics capabilities for representing seasonal data, including boxplots for
  seasonal parameters, and bars for summed normals. There are many specific
  functions related to climatology, including precipitation normals,
  temperature normals, cumulative precipitation departures and precipitation
  interarrivals. However, this package is designed to represent any
  time-varying parameter with a discernible seasonal signal, such as found
  in hydrology and ecology.
	"""
	
	homepage = "https://github.com/mwtoews/seas"
	cran = "seas" 

	version("0.6-0", md5="f4d483b04ec88b608831def27d87ff70")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
