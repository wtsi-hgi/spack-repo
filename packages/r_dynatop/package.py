# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDynatop(RPackage):
	"""An Implementation of Dynamic TOPMODEL Hydrological Model in R

	An R implementation and enhancement of the Dynamic TOPMODEL semi-distributed hydrological model originally proposed by Beven and Freer (2001) <doi:10.1002/hyp.252>. The 'dynatop' package implements code for simulating models which can be created using the 'dynatopGIS' package.
	"""
	
	homepage = "https://waternumbers.github.io/dynatop/"
	cran = "dynatop" 

	version("0.2.3", md5="8fbcd269834fde1ec10eca1d7a3dd014")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
