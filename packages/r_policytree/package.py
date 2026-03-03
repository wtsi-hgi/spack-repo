# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPolicytree(RPackage):
	"""Policy Learning via Doubly Robust Empirical Welfare Maximization
over Trees

	Learn optimal policies via doubly robust empirical
 welfare maximization over trees. Given doubly robust reward estimates, this package
 finds a rule-based treatment prescription policy, where the policy takes the form of
 a shallow decision tree that is globally (or close to) optimal.
	"""
	
	homepage = "https://github.com/grf-labs/policytree"
	cran = "policytree" 

	version("1.2.2", md5="314e19a3a2a84a1745d73bd84b1d88ae")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-grf@2:", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
