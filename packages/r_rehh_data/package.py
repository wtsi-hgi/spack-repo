# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRehhData(RPackage):
	"""Data Only: Searching for Footprints of Selection using Haplotype
Homozygosity Based Tests

	Contains example data for the 'rehh' package. 
	"""
	
	cran = "rehh.data" 

	version("1.0.0", md5="b71e5bb7ce581dfd6e7fd04398f0f8f6")

	depends_on("r@2.10:", type=("build", "run"))
