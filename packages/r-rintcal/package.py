# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRintcal(RPackage):
	"""Radiocarbon Calibration Curves

	The IntCal20 radiocarbon calibration curves (Reimer et al. 2020 <doi:10.1017/RDC.2020.68>) are provided as a data package, together with previous IntCal curves (IntCal13, IntCal09, IntCal04, IntCal98) and postbomb curves. Also provided are functions to copy the curves into memory, to plot the curves and their underlying data, to calibrate radiocarbon dates and to transform between different radiocarbon 'domains'.
	"""
	
	cran = "rintcal" 

	version("0.6.4", md5="2f0932c06dac48cd5b44e0384433b2e0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
