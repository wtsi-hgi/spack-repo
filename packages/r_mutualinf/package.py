# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMutualinf(RPackage):
	"""Computation and Decomposition of the Mutual Information Index

	The Mutual Information Index (M) introduced to social science literature by
    Theil and Finizza (1971) <doi:10.1080/0022250X.1971.9989795> is a multigroup
    segregation measure that is highly decomposable and that according to Frankel
    and Volij (2011) <doi:10.1016/j.jet.2010.10.008> and Mora and Ruiz-Castillo
    (2011) <doi:10.1111/j.1467-9531.2011.01237.x> satisfies the Strong Unit
    Decomposability and Strong Group Decomposability properties. This package allows
    computing and decomposing the total index value into its "between" and
    "within" terms. These last terms can also be decomposed into their
    contributions, either by group or unit characteristics. The factors that produce
    each "within" term can also be displayed at the user's request. The results can
    be computed considering a variable or sets of variables that define separate
    clusters.
	"""
	
	homepage = "https://github.com/RafaelFuentealbaC/mutualinf"
	cran = "mutualinf" 

	version("1.2.2", md5="2fddfa58d974aea030d6f4f90d6a20fc")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-runner", type=("build", "run"))
