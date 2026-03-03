# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REtm(RPackage):
	"""Empirical Transition Matrix

	The etm (empirical transition matrix) package permits to estimate the matrix of transition probabilities for any time-inhomogeneous multi-state model with finite state space using the Aalen-Johansen estimator. Functions for data preparation and for displaying are also included (Allignol et al., 2011 <doi:10.18637/jss.v038.i04>). Functionals of the Aalen-Johansen estimator, e.g., excess length-of-stay in an intermediate state, can also be computed (Allignol et al. 2011 <doi:10.1007/s00180-010-0200-x>).
	"""
	
	cran = "etm" 

	version("1.1.1", md5="3a462f6d9b5071d6ff692d42e719f6fc")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
