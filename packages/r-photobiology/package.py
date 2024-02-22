# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhotobiology(RPackage):
	"""Photobiological Calculations

	Definitions of classes, methods, operators and functions for use 
    in photobiology and radiation meteorology and climatology. Calculation of
    effective (weighted) and not-weighted irradiances/doses, fluence rates,
    transmittance, reflectance, absorptance, absorbance and diverse ratios and 
    other derived quantities from spectral data. Local maxima and minima: peaks,
    valleys and spikes. Conversion between energy-and photon-based units. 
    Wavelength interpolation. Astronomical calculations related solar angles and 
    day length. Colours and vision. This package is part of the 'r4photobiology' 
    suite, Aphalo, P. J. (2015) <doi:10.19232/uv4pb.2015.1.14>.
	"""
	
	homepage = "https://docs.r4photobiology.info/photobiology/"
	cran = "photobiology" 

	version("0.11.0", md5="c9b3e4f28d22f89b2683e08d640da55e")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-polynom@1.4.1:", type=("build", "run"))
	depends_on("r-tibble@3.1.6:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-lubridate@1.9:", type=("build", "run"))
	depends_on("r-plyr@1.8.7:", type=("build", "run"))
	depends_on("r-dplyr@1.0.9:", type=("build", "run"))
	depends_on("r-tidyr@1.2:", type=("build", "run"))
	depends_on("r-splus2r@1.3.3:", type=("build", "run"))
	depends_on("r-zoo@1.8.8:", type=("build", "run"))
	depends_on("r-rlang@1.0.4:", type=("build", "run"))
