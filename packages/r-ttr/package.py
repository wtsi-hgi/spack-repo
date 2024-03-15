# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTtr(RPackage):
	"""Technical Trading Rules.

	A collection of over 50 technical indicators for creating technical trading
	rules. The package also provides fast implementations of common
	rolling-window functions, and several volatility calculations."""

	cran = "TTR"

	version("0.24.4", md5="6c9c67ca98639d233f89d4bb002b6c8f")

	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
