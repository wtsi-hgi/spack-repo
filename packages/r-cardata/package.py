# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCardata(RPackage):
	"""Companion to Applied Regression Data Sets.

	Datasets to Accompany J. Fox and S. Weisberg, An R Companion to Applied
	Regression, Third Edition, Sage (2019)."""

	cran = "carData"

	version("3.0-4", sha256="cda6f5e3efc1d955a4a0625e9c33f90d49f5455840e88b3bd757129b86044724")
	version("3.0-2", sha256="3b5c4eff1cc1e456a5331084774503eaa06cf61fb7acf6b9e8a6bfabd5735494")
	version("3.0-5", md5="88dc01e1d94d67652d4c4c38d33a8981")

	depends_on("r@3.5:", type=("build", "run"))
