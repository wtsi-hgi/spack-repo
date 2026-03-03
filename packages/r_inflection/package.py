# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInflection(RPackage):
	"""Finds the Inflection Point of a Curve

	Implementation of methods Extremum Surface Estimator (ESE) and 
   Extremum Distance Estimator (EDE) to identify the inflection point of a curve .
   Christopoulos, DT (2014) <doi:10.48550/arXiv.1206.5478> .
   Christopoulos, DT (2016) <https://veltech.edu.in/wp-content/uploads/2016/04/Paper-04-2016.pdf> .
   Christopoulos, DT (2016) <doi:10.2139/ssrn.3043076> .
	"""
	
	homepage = "https://CRAN.R-project.org/package=inflection"
	cran = "inflection" 

	version("1.3.6", md5="92802bf228a3ce04bb912cde4b4614c5")

