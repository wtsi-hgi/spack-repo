# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsatscan(RPackage):
	"""Tools, Classes, and Methods for Interfacing with 'SaTScan'
Stand-Alone Software

	'SaTScan'(TM) <https://www.satscan.org> is software for finding regions in 
    Time, Space, or Time-Space that have excess risk, based on scan statistics, and 
	uses Monte Carlo hypothesis testing to generate P-values for these regions.  The 
	'rsatscan' package provides functions for writing R data frames in 
	'SaTScan'-readable formats, for setting 'SaTScan' parameters, for running 'SaTScan' in 
	the OS, and for reading the files that 'SaTScan' creates.  
	"""
	
	homepage = "https://www.satscan.org"
	cran = "rsatscan" 

	version("1.0.7", md5="99e7a68fe46071ef753e487a38a0feb5")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
