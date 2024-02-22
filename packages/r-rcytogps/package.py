# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcytogps(RPackage):
	"""Using Cytogenetics Data in R

	Defines classes and methods to process text-based
  cytogenetics using the CytoGPS web site, then import the results
  into R for further analysis and graphing.
	"""
	
	homepage = "http://oompa.r-forge.r-project.org/"
	cran = "RCytoGPS" 

	version("1.2.5", md5="3d607ebbea051610218c3018ffbe6794")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
