# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAgilp(RPackage):
	"""Agilent expression array processing package.

	More about what it does (maybe more than one line)."""

	bioc = "agilp"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/agilp_3.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/agilp/agilp_3.34.0.tar.gz"]

	version("3.34.0", md5="21b54a703747520483657dd63288f403")

	depends_on("r@2.14:", type=("build", "run"))
