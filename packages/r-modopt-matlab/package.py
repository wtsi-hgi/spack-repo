# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModoptMatlab(RPackage):
	"""'MatLab'-Style Modeling of Optimization Problems

	'MatLab'-Style Modeling of Optimization Problems with 'R'. This package provides a set of convenience functions to transform a 'MatLab'-style optimization modeling structure to its 'ROI' equivalent.
	"""
	
	homepage = "http://www.finance-r.com/"
	cran = "modopt.matlab" 

	version("1.0-2", md5="cb1e10c5ab24141fb609c03e38492d3e")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-roi", type=("build", "run"))
	depends_on("r-roi-plugin-glpk", type=("build", "run"))
	depends_on("r-roi-plugin-quadprog", type=("build", "run"))
