# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTbest(RPackage):
	"""Tree Branches Evaluated Statistically for Tightness

	Our method introduces mathematically well-defined measures for tightness of branches in a hierarchical tree. Statistical significance of the findings is determined, for all branches of the tree, by performing permutation tests, optionally with generalized Pareto p-value estimation.
	"""
	
	cran = "TBEST" 

	version("5.2", md5="7b577df2b36053e818475d2f157f2f63")

	depends_on("r-signal", type=("build", "run"))
	depends_on("r-fdrtool", type=("build", "run"))
