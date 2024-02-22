# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnakecase(RPackage):
	"""Convert Strings into any Case.

	A consistent, flexible and easy to use tool to parse and convert strings
	into cases like snake or camel among others."""

	cran = "snakecase"

	version("0.11.1", md5="3e5cbad0056783cff60d05eb75881f62")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
