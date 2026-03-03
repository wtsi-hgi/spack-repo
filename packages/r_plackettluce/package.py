# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlackettluce(RPackage):
	"""Plackett-Luce Models for Rankings

	Functions to prepare rankings data and fit the Plackett-Luce model
    jointly attributed to Plackett (1975) <doi:10.2307/2346567> and Luce
    (1959, ISBN:0486441369). The standard Plackett-Luce model is generalized
    to accommodate ties of any order in the ranking. Partial rankings, in which
    only a subset of items are ranked in each ranking, are also accommodated in
    the implementation. Disconnected/weakly connected networks implied by the
    rankings may be handled by adding pseudo-rankings with a hypothetical item.
    Optionally, a multivariate normal prior may be set on the log-worth
    parameters and ranker reliabilities may be incorporated as proposed by
    Raman and Joachims (2014) <doi:10.1145/2623330.2623654>. Maximum a
    posteriori estimation is used when priors are set. Methods are provided to
    estimate standard errors or quasi-standard errors for inference as well as
    to fit Plackett-Luce trees. See the package website or vignette for further
    details.
	"""
	
	homepage = "https://hturner.github.io/PlackettLuce/"
	cran = "PlackettLuce" 

	version("0.4.3", md5="aca97f41de5680c3d62ee039f9a55316")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cvxr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-partykit", type=("build", "run"))
	depends_on("r-psychotools", type=("build", "run"))
	depends_on("r-psychotree", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-qvcalc", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
