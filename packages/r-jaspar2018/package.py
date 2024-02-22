# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJaspar2018(RPackage):
	"""Data package for JASPAR 2018.

	Data package for JASPAR 2018. To search this databases, please use the
	package TFBSTools (>= 1.15.6)."""

	bioc = "JASPAR2018"
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/JASPAR2018_1.1.1.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/JASPAR2018/JASPAR2018_1.1.1.tar.gz"]

	version("1.1.1", md5="d91fce6ea0dc9fa6a3be6ebc05c1af5d", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/JASPAR2018_1.1.1.tar.gz")

	depends_on("r@3.4:", type=("build", "run"))

	# annotation