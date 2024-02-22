# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcpsrdata(RPackage):
	"""Reproducible Data Retrieval from the ICPSR Archive

	Reproducible, programmatic retrieval of datasets from the
    Inter-university Consortium for Political and Social Research archive.
	"""
	
	homepage = "https://github.com/fsolt/icpsrdata"
	cran = "icpsrdata" 

	version("0.6.1", md5="7598937c387abbd51d1343724771ac77")

	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
