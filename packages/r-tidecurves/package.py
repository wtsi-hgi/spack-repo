# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidecurves(RPackage):
	"""Analysis and Prediction of Tides

	Tidal analysis of evenly spaced observed time series (time step 1 to 60 min) with or
    without shorter gaps using the harmonic representation of inequalities.
    The analysis should preferably cover an observation period of at least 19 years.
    For shorter periods low frequency constituents are not taken into account, in accordance with the Rayleigh-Criterion.
    The main objective of this package is to synthesize or predict a tidal time series.
	"""
	
	cran = "TideCurves" 

	version("0.0.5", md5="8cae1a161fdcf0f0ea7ad7f226b66d75")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-chron@2.3.56:", type=("build", "run"))
	depends_on("r-data-table@1.14:", type=("build", "run"))
	depends_on("r-fields@11.6:", type=("build", "run"))
