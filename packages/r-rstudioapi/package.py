# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRstudioapi(RPackage):
	"""Safely Access the RStudio API.

	Access the RStudio API (if available) and provide informative error
	messages when it's not."""

	cran = "rstudioapi"

	version("0.15.0", md5="25e0dafe967089165efab98158a0d6da")

