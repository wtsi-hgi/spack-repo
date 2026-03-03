# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDjl(RPackage):
	"""Distance Measure Based Judgment and Learning

	Implements various decision support tools related to the Econometrics & Technometrics.
             Subroutines include correlation reliability test, Mahalanobis distance measure for outlier detection, combinatorial search (all possible subset regression), non-parametric efficiency analysis measures: DDF (directional distance function), DEA (data envelopment analysis), HDF (hyperbolic distance function), SBM (slack-based measure), and SF (shortage function), benchmarking, Malmquist productivity analysis, risk analysis, technology adoption model, new product target setting, network DEA, dynamic DEA, intertemporal budgeting, etc.
	"""
	
	cran = "DJL" 

	version("3.9", md5="8ea81f54d72c205b1ebd480bf197bc9c")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-lpsolveapi", type=("build", "run"))
