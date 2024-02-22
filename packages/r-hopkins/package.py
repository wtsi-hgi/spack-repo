# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHopkins(RPackage):
	"""Calculate Hopkins Statistic for Clustering

	Calculate Hopkins statistic to assess the clusterability of data. See Wright (2023) <doi:10.32614/RJ-2022-055>.
	"""
	
	homepage = "https://kwstat.github.io/hopkins/"
	cran = "hopkins" 

	version("1.1", md5="ef03c24f57b39c201589de4a15ca5dd7")

	depends_on("r-donut", type=("build", "run"))
	depends_on("r-pdist", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
