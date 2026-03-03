# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRddapp(RPackage):
	"""Regression Discontinuity Design Application

	Estimation of both single- and multiple-assignment Regression Discontinuity Designs 
    (RDDs). Provides both parametric (global) and non-parametric (local) estimation choices for
    both sharp and fuzzy designs, along with power analysis and assumption checks. 
    Introductions to the underlying logic and analysis of RDDs are in 
    Thistlethwaite, D. L., Campbell, D. T. (1960) <doi:10.1037/h0044319> and
    Lee, D. S., Lemieux, T. (2010) <doi:10.1257/jel.48.2.281>.
	"""
	
	cran = "rddapp" 

	version("1.3.2", md5="d797f5e686d8d32babf1e1489600ac85")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-aer@1.2.5:", type=("build", "run"))
	depends_on("r-sandwich@2.3.4:", type=("build", "run"))
	depends_on("r-lmtest@0.9.35:", type=("build", "run"))
	depends_on("r-formula@1.2.1:", type=("build", "run"))
	depends_on("r-shiny@0.14:", type=("build", "run"))
	depends_on("r-r-utils@2.6:", type=("build", "run"))
	depends_on("r-plot3d@1.1.1:", type=("build", "run"))
	depends_on("r-sp@1.3.1:", type=("build", "run"))
	depends_on("r-dt@0.2:", type=("build", "run"))
