# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTseries(RPackage):
	"""Time series analysis and computational finance."""

	cran = "tseries"

	version("0.10-55", md5="48f91be31447054c9d104715f0557e9b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-quantmod@0.4.9:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
