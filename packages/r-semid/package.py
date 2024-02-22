# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSemid(RPackage):
	"""Identifiability of Linear Structural Equation Models

	Provides routines to check identifiability or non-identifiability
    of linear structural equation models as described in Drton, Foygel, and
    Sullivant (2011) <doi:10.1214/10-AOS859>, Foygel, Draisma, and Drton (2012) 
    <doi:10.1214/12-AOS1012>, and other works. The routines are based on the graphical 
    representation of structural equation models.
	"""
	
	homepage = "https://github.com/Lucaweihs/SEMID"
	cran = "SEMID" 

	version("0.4.1", md5="cccede6b22f3cd2d8a9201405c757742")

	depends_on("r-r-oo@1.20:", type=("build", "run"))
	depends_on("r-r-methodss3", type=("build", "run"))
	depends_on("r-igraph@1.0.1:", type=("build", "run"))
	depends_on("r-r-utils@2.3:", type=("build", "run"))
