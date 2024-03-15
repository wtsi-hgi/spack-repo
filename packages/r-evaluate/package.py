# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvaluate(RPackage):
	"""Parsing and Evaluation Tools that Provide More Details than the Default.

	Parsing and evaluation tools that make it easy to recreate the command
	line behaviour of R."""

	cran = "evaluate"

	license("MIT")

	version("0.23", md5="f95f31851168165421c128109668a213")

	depends_on("r@3.0.2:", type=("build", "run"))
