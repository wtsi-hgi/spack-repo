# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatamojo(RPackage):
	"""Reshape Data Table

	A grammar of data manipulation with 'data.table', providing a consistent a series of utility functions that help you solve the most common data manipulation challenges.
	"""
	
	cran = "dataMojo" 

	version("1.0.0", md5="b84f06bcc0d69a7a180e4ddc5d578cf2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
