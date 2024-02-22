# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRxylib(RPackage):
	"""Import XY-Data into R

	Provides access to the 'xylib' C library for to import xy 
  data from powder diffraction, spectroscopy and other experimental methods.
	"""
	
	homepage = "https://github.com/R-Lum/rxylib"
	cran = "rxylib" 

	version("0.2.12", md5="ff780eb082777227610ca1a7b34d9383")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rcpp@1.0.10:", type=("build", "run"))
	depends_on("r-bh@1.81:", type=("build", "run"))
