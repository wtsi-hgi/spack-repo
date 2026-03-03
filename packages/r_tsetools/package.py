# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsetools(RPackage):
	"""Manage Data from Stock Exchange Markets

	Tools to perform some descriptive data analysis for assets. Manage the portfolio and capital of assets. It also downloads and organizes data from the Tehran Stock Exchange (TSE).
	"""
	
	cran = "TSEtools" 

	version("0.2.2", md5="7ff5688746a66cc1e32efd137dd23443")

	depends_on("r-xts", type=("build", "run"))
	depends_on("r-quantmod", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
