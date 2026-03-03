# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorels(RPackage):
	"""R Binding for the 'Certifiably Optimal RulE ListS (Corels)'
Learner

	The 'Certifiably Optimal RulE ListS (Corels)' learner by
 Angelino et al described in <arXiv:1704.01701> provides interpretable decision
 rules with an optimality guarantee, and is made available to R with this package.
 See the file 'AUTHORS' for a list of copyright holders and contributors.
	"""
	
	homepage = "https://github.com/corels/rcppcorels"
	cran = "corels" 

	version("0.0.4", md5="1079c5082b275759cf7eaa89b77580a8")

	depends_on("r-rcpp", type=("build", "run"))
