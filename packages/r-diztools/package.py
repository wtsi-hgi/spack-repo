# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiztools(RPackage):
	"""Lightweight Utilities for 'DIZ' R Package Development

	Lightweight utility functions used for the R package
    development infrastructure inside the data integration centers ('DIZ')
    to standardize and facilitate repetitive tasks such as setting up a
    database connection or issuing notification messages and to avoid
    redundancy.
	"""
	
	homepage = "https://github.com/miracum/misc-diztools"
	cran = "DIZtools" 

	version("1.0.1", md5="d11fa87c9af290831c05c7558da2703b")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-clear", type=("build", "run"))
	depends_on("r-config", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-logger", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-parsedate", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
