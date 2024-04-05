# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImpactr(RPackage):
	"""Mechanical Loading Prediction Through Accelerometer Data

	Functions to read, process and analyse accelerometer
    data related to mechanical loading variables. This package is
    developed and tested for use with raw accelerometer data from
    triaxial 'ActiGraph' <https://theactigraph.com> accelerometers.
	"""
	
	homepage = "https://lveras.com/impactr/"
	cran = "impactr" 

	version("0.4.2", md5="44b1f878f87e30e86abe5a40ebb3119a")
	version("0.4.1", md5="3526fce648cd674536299e5356af7d2e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-lvmisc", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang@0.4.6:", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-toordinal", type=("build", "run"))
	depends_on("r-vroom", type=("build", "run"))
