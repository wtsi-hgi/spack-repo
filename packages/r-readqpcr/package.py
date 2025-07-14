# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReadqpcr(RPackage):
	"""Read qPCR data

	The package provides functions to read raw RT-qPCR data of different platforms.
	"""
	
	homepage = "http://www.bioconductor.org/packages/release/bioc/html/ReadqPCR.html"
	bioc = "ReadqPCR"

	version("1.54.0", commit="aa057523b941c2a4eeb8eef5701eb2b68975dc84")
	version("1.48.0", commit="d01e81cd42a665cb39a246d79c2ee69137143dca")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
