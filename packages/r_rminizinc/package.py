# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRminizinc(RPackage):
	"""R Interface to 'MiniZinc'

	Constraint optimization, or constraint programming, is the name given to identifying
  feasible solutions out of a very large set of candidates, where the problem can be modeled in terms 
  of arbitrary constraints. 'MiniZinc' is a free and open-source constraint modeling language. 
  Constraint satisfaction and discrete optimization problems can be formulated in a high-level 
  modeling language. Models are compiled into an intermediate representation that is understood by a
  wide range of solvers. 'MiniZinc' itself provides several solvers, for instance 'GeCode'. R users 
  can use the package to solve constraint programming problems without using 'MiniZinc' directly, 
  modify existing 'MiniZinc' models and also create their own models.
	"""
	
	homepage = "https://github.com/acharaakshit/RMiniZinc"
	cran = "rminizinc" 

	version("0.0.8", md5="87212c85b3fdf62f5820a0eb4125a21c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("pandoc@1.14:", type=("build", "link", "run"))
