# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFractalregression(RPackage):
	"""Performs Fractal Analysis and Fractal Regression

	Various functions for performing fractal and multifractal analysis including performing fractal regression. Please refer to Peng and colleagues (1994) <doi:10.1103/physreve.49.1685>, Kantelhardt and colleagues (2002)<doi:10.1016/S0378-4371(02)01383-3>, and Likens and colleagues (2019) <doi:10.1016/j.physa.2019.121580>.
	"""
	
	cran = "fractalRegression" 

	version("1.2", md5="011a2439a7112e5b71e858ccea5590d1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-colorramps", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
