# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrtsize(RPackage):
	"""Sample Size Estimation Functions for Cluster Randomized Trials

	Sample size estimation in cluster (group) randomized trials.  Contains traditional power-based methods, empirical smoothing (Rotondi and Donner, 2009), and updated meta-analysis techniques (Rotondi and Donner, 2012).
	"""
	
	cran = "CRTSize" 

	version("1.2", md5="f460e127051bbbc1e56029089e4902f4")

	depends_on("r@2.1:", type=("build", "run"))
