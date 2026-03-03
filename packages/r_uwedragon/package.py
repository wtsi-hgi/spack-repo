# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUwedragon(RPackage):
	"""Data Research, Access, Governance Network : Statistical
Disclosure Control

	A tool for checking how much information is disclosed when
    reporting summary statistics.
	"""
	
	cran = "uwedragon" 

	version("0.1.0", md5="08d18422420b1bdcf9e6978d95c69a88")

	depends_on("r-gtools", type=("build", "run"))
