# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntcal(RPackage):
	"""Radiocarbon Calibration Curves

	The IntCal20 radiocarbon calibration curves (Reimer et al. 2020 <doi:10.1017/RDC.2020.68>) are provided here in a single data package, together with previous IntCal curves (IntCal13, IntCal09, IntCal04, IntCal98) and postbomb curves. Also provided are functions to copy the curves into memory, and to plot the curves and their underlying data, as well as functions to calibrate radiocarbon dates.
	"""
	
	cran = "IntCal" 

	version("0.3.1", md5="70214ce91097db1385dc54621672acd4")

