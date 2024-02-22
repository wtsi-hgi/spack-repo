# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrio(RPackage):
	"""Basic R Input Output.

	Functions to handle basic input output, these functions always read and
	write UTF-8 (8-bit Unicode Transformation Format) files and provide more
	explicit control over line endings."""

	cran = "brio"

	version("1.1.4", md5="e18151323dcddd193fac454f70f138f1")

	depends_on("r@3.6:", type=("build", "run"))
