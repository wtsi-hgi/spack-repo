# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFansi(RPackage):
	"""ANSI Control Sequence Aware String Functions.

	Counterparts to R string manipulation functions that account for the
	effects of ANSI text formatting control sequences."""

	cran = "fansi"

	license("GPL-2.0-only OR GPL-3.0-only")

	version("1.0.6", md5="27eb3b066918811ce7080f45b18eda04")

	depends_on("r@3.1:", type=("build", "run"))
