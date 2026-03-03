# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIemisc(RPackage):
	"""Irucka Embry's Miscellaneous Functions

	A collection of Irucka Embry's miscellaneous functions
    (Engineering Economics, Civil & Environmental/Water Resources Engineering,
    Construction Measurements, GNU Octave compatible functions, Python
    compatible function, Trigonometric functions in degrees and function in
    radians, Geometry, Statistics, Mortality Calculators, Quick Search, etc.).
	"""
	
	homepage = "https://gitlab.com/iembry/iemisc"
	cran = "iemisc" 

	version("1.0.4", md5="967101f420f201f031a777e81f1e2f5e")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-iemiscdata", type=("build", "run"))
	depends_on("r-gsubfn@0.7:", type=("build", "run"))
	depends_on("r-fpcompare", type=("build", "run"))
	depends_on("r-units@0.7.0:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-rivr@1.2.2:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-chem-databases", type=("build", "run"))
	depends_on("r-ramify", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-data-table@1.10.2:", type=("build", "run"))
	depends_on("r-measurements", type=("build", "run"))
	depends_on("r-roperators", type=("build", "run"))
	depends_on("r-berryfunctions", type=("build", "run"))
	depends_on("r-round", type=("build", "run"))
	depends_on("r-usa-state-boundaries@1.0.1:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-matlab", type=("build", "run"))
	depends_on("r-sjmisc", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-anytime", type=("build", "run"))
	depends_on("r-qdapregex", type=("build", "run"))
	depends_on("r-mgsub", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-matlab2r", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
