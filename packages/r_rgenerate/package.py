# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgenerate(RPackage):
	"""Tools to Generate Vector Time Series

	A method 'generate()' is implemented in this package for the random
    generation of vector time series according to models obtained by 'RMAWGEN',
    'vars' or other packages.  This package was created to generalize the
    algorithms of the 'RMAWGEN' package for the analysis and generation of any
    environmental vector time series.
	"""
	
	homepage = "https://github.com/ecor/RGENERATE"
	cran = "RGENERATE" 

	version("1.3.7", md5="a0d1a7373556368946004d4ea225d08f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rmawgen", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
