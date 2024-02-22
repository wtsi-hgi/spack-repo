# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMasscor(RPackage):
	"""Mass Measurement Corrections

	Mass measurement corrections and uncertainties using calibration
    data, as recommended by EURAMET's guideline No. 18 (2015) 
    ISBN:978-3-942992-40-4 . The package provides classes, functions, and 
    methods for storing information contained in calibration certificates
    and converting balance readings to both conventional mass and real mass.
    For the latter, the Magnitude of the Air Buoyancy Correction factor employs
    models (such as the CIMP-2007 formula revised by Picard, Davis, Gläser, and
    Fujii (2008) <doi:10.1088/0026-1394/45/2/004>) to estimate the local air
    density using measured environmental conditions.
	"""
	
	cran = "masscor" 

	version("0.0.7.1", md5="c58c4d2c999a9efe4311e190628ed3b1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-metrology", type=("build", "run"))
