# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROmpr(RPackage):
	"""Model and Solve Mixed Integer Linear Programs

	Model mixed integer linear programs in an algebraic way directly in R.
             The model is solver-independent and thus offers the possibility
             to solve a model with different solvers. It currently only supports
             linear constraints and objective functions. See the 'ompr'
             website <https://dirkschumacher.github.io/ompr/> for more information,
             documentation and examples.
	"""
	
	homepage = "https://github.com/dirkschumacher/ompr"
	cran = "ompr" 

	version("1.0.4", md5="b76c82d19284810ba3bd51b6889624cd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("r-rlang@0.2:", type=("build", "run"))
	depends_on("r-listcomp@0.4:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-fastmap", type=("build", "run"))
