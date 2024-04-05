# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWflo(RPackage):
	"""Data Set and Helper Functions for Wind Farm Layout Optimization
Problems

	Provides a convenient data set, a set of helper functions, and a benchmark function for
    economically (profit) driven wind farm layout optimization. This enables researchers in the field
    of the NP-hard (non-deterministic polynomial-time hard) problem of wind farm layout optimization
    to focus on their optimization methodology contribution and also provides a realistic benchmark
    setting for comparability among contributions. See Croonenbroeck, Carsten & Hennecke, David (2020)
    <doi:10.1016/j.energy.2020.119244>.
	"""
	
	cran = "wflo" 

	version("1.9", md5="6a15a1f3feeee1082e13f1d186fe805c")
	version("1.8", md5="6dc75099505f99a14212ed0be49e2f1f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-emstreer", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
