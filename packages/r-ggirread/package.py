# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgirread(RPackage):
	"""Wearable Accelerometer Data File Readers

	Reads data collected from wearable acceleratometers as used in sleep and physical activity research. Currently supports file formats: binary data from 'GENEActiv' <https://activinsights.com/>, .bin-format from GENEA devices (not for sale), and .cwa-format from 'Axivity' <https://axivity.com>. Primarily designed to complement R package GGIR <https://CRAN.R-project.org/package=GGIR>.
	"""
	
	homepage = "https://github.com/wadpac/GGIRread/"
	cran = "GGIRread" 

	version("1.0.0", md5="c2c8b472de870dba6c99b971d53a6437")
	version("0.3.3", md5="6e982afb89c200a9b5136dee786faa7a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matlab", type=("build", "run"))
	depends_on("r-bitops", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
