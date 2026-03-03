# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGreymodel(RPackage):
	"""Fitting and Forecasting of Grey Model

	Testing, Implementation and Forecasting of Grey Model (GM(1, 1)). For method details see Hsu, L. and Wang, C. (2007). <doi:10.1016/j.techfore.2006.02.005>. 
	"""
	
	cran = "GreyModel" 

	version("0.1.0", md5="892135259685848ccd0e16ef45314c54")

	depends_on("r@2.10:", type=("build", "run"))
