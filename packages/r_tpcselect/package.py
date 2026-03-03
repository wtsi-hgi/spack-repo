# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTpcselect(RPackage):
	"""Variable Selection via Threshold Partial Correlation

	A threshold partial correlation approach to selecting 
             important variables in linear models of L. and others (2017) at
             <doi:10.5705/ss.202015.0473>, and in partial linear models
             of L. and others (2018) at <doi:10.1016/j.jmva.2018.06.005>. 
             This package also extends the PC-simple algorithm of
             B. and others (2010) at <doi:10.1093/biomet/asq008> to 
             partial linear models.
	"""
	
	cran = "TPCselect" 

	version("0.8.3", md5="c64058fce1d3b8c561e3b9671162e453")

	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
