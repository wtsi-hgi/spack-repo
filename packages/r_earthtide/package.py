# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REarthtide(RPackage):
	"""Parallel Implementation of 'ETERNA 3.40' for Prediction and
Analysis of Earth Tides

	This is a port of 'Fortran ETERNA 3.4' 
             <http://igets.u-strasbg.fr/soft_and_tool.php> by H.G. Wenzel
             for calculating synthetic Earth tides using the 
             Hartmann and Wenzel (1994) <doi:10.1029/95GL03324> or 
             Kudryavtsev (2004) <doi:10.1007/s00190-003-0361-2> tidal catalogs. 
	"""
	
	homepage = "https://github.com/jkennel/earthtide"
	cran = "earthtide" 

	version("0.1.2", md5="0b2cb3a17419eae876b8fa18824ea1a5")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp@1:", type=("build", "run"))
	depends_on("r-r6@2.3:", type=("build", "run"))
	depends_on("r-rcppthread", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
