# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsdisaggregation(RPackage):
	"""High-Dimensional Temporal Disaggregation

	First - Generates (potentially high-dimensional) high-frequency and low-frequency series for simulation studies in temporal disaggregation; Second - a toolkit utilizing temporal disaggregation and benchmarking techniques with a low-dimensional matrix of indicator series previously proposed in Dagum and Cholette (2006, ISBN:978-0-387-35439-2) ; and Third - novel techniques proposed by Mosley, Gibberd and Eckley (2021) <arXiv:2108.05783> for disaggregating low-frequency series in the presence of high-dimensional indicator matrices.
	"""
	
	cran = "TSdisaggregation" 

	version("2.0.0", md5="d8d09ac30d1f5f54982631eb1ba39ef4")

	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-lars", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
