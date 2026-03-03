# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRacir(RPackage):
	"""Rapid A/Ci Response (RACiR) Data Analysis

	Contains functions useful for reading in Licor 6800 files,
    correcting and analyzing rapid A/Ci response (RACiR) data. Requires some
    user interaction to adjust the calibration (empty chamber) data file to 
    a useable range. Calibration uses a 1st to 5th order polynomial as 
    suggested in Stinziano et al. (2017) <doi:10.1111/pce.12911>.
    Data can be processed individually or batch processed for all files paired
    with a given calibration file. RACiR is a trademark of LI-COR Biosciences,
    and used with permission.
	"""
	
	homepage = "https://github.com/jstinzi/racir"
	cran = "racir" 

	version("2.0.0", md5="45da4233364dab1e2bfbb5c5c245fb91")

	depends_on("r@4:", type=("build", "run"))
