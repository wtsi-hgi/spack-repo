# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJuicr(RPackage):
	"""Automated and Manual Extraction of Numerical Data from
Scientific Images

	Provides a GUI interface for automating data extraction from 
  multiple images containing scatter and bar plots, semi-automated tools to tinker 
  with extraction attempts, and a fully-loaded point-and-click manual extractor 
  with image zoom, calibrator, and classifier. Also provides detailed and 
  R-independent extraction reports as fully-embedded .html records.
	"""
	
	homepage = "http://lajeunesse.myweb.usf.edu/"
	cran = "juicr" 

	version("0.1", md5="951d9f537a3715189893ae044882a0a6")

	depends_on("r@3.3.2:", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("tcl", type=("build", "link", "run"))
	depends_on("tk", type=("build", "link", "run"))
