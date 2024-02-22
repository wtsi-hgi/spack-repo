# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIr(RPackage):
	"""Functions to Handle and Preprocess Infrared Spectra

	
  Functions to import and handle infrared spectra (import from '.csv' and
  Thermo Galactic's '.spc', baseline correction, binning, clipping,
  interpolating, smoothing, averaging, adding, subtracting, dividing, 
  multiplying, plotting).
	"""
	
	homepage = "https://henningte.github.io/ir/"
	cran = "ir" 

	version("0.2.1", md5="c0523e9eb900b3bdea8dddbe6d17fb30")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-chemospec@5.2.12:", type=("build", "run"))
	depends_on("r-hyperspec@0.99.20200527:", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-baseline", type=("build", "run"))
