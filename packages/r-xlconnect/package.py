# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXlconnect(RPackage):
	"""Excel Connector for R.

	Provides comprehensive functionality to read, write and format Excel
	data."""

	cran = "XLConnect"

	version("1.0.8", md5="02936bb222965b561be091eb869aa9b0")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rjava@1.0.1:", type=("build", "run"))
	depends_on("openjdk@8:", type=("build", "link", "run"))
