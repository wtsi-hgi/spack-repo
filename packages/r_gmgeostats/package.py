# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGmgeostats(RPackage):
	"""Geostatistics for Compositional Analysis

	Support for geostatistical analysis of multivariate data, 
         in particular data with restrictions, e.g. positive amounts, 
         compositions, distributional data, microstructural data, etc. 
         It includes descriptive analysis and modelling for such data, both 
         from a two-point Gaussian perspective and multipoint perspective.
         The methods mainly follow Tolosana-Delgado, Mueller and van den
         Boogaart (2018) <doi:10.1007/s11004-018-9769-3>.
	"""
	
	homepage = "https://codebase.helmholtz.cloud/geomet/gmGeostats"
	cran = "gmGeostats" 

	version("0.11.3", md5="d206ae971fe6b78aab80007e3bbe0515")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-gstat", type=("build", "run"))
	depends_on("r-compositions@2:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
