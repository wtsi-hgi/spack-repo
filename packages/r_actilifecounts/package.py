# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RActilifecounts(RPackage):
	"""Generate Activity Counts from Raw Accelerometer Data

	A tool to obtain activity counts, originally a translation of the 
  'python' package 'agcounts' <https://github.com/actigraph/agcounts>. This tool
  allows the processing of data from any accelerometer brand, with a more flexible 
  approach to handle different sampling frequencies.
	"""
	
	homepage = "https://github.com/jhmigueles/actilifecounts"
	cran = "actilifecounts" 

	version("1.1.1", md5="4a86bca3a94ca789bdf4bfc56ac5f9dd")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-gsignal", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-ggirread", type=("build", "run"))
