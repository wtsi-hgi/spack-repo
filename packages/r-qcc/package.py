# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQcc(RPackage):
	"""Quality Control Charts

	Shewhart quality control charts for continuous, attribute and count data. Cusum and EWMA charts. Operating characteristic curves. Process capability analysis. Pareto chart and cause-and-effect chart. Multivariate control charts.
	"""
	
	homepage = "https://github.com/luca-scr/qcc"
	cran = "qcc" 

	version("2.7", md5="e16783e0accb474c542a0b3d07352431")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
