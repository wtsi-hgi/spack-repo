# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGewist(RPackage):
	"""Gene Environment Wide Interaction Search Threshold

	This 'GEWIST' package provides statistical tools to efficiently optimize SNP prioritization for gene-gene and gene-environment interactions.
	"""
	
	bioc = "GEWIST"

	version("1.52.0", commit="a3937a7de693d3ce2aa8782c865bcbf5d0e906e6")
	version("1.46.0", commit="321106805b5df05f716f37dc460e825b204a0f2d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
