# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPks(RPackage):
	"""Probabilistic Knowledge Structures

	Fitting and testing probabilistic knowledge structures,
  especially the basic local independence model (BLIM, Doignon & Flamagne,
  1999) and the simple learning model (SLM), using the minimum discrepancy
  maximum likelihood (MDML) method (Heller & Wickelmaier, 2013
  <doi:10.1016/j.endm.2013.05.145>).
	"""
	
	homepage = "http://www.mathpsy.uni-tuebingen.de/wickelmaier/"
	cran = "pks" 

	version("0.6-0", md5="3a460e7130ee838ed8834ec4a6d9438e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sets", type=("build", "run"))
