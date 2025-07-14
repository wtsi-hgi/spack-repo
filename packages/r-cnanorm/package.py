# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCnanorm(RPackage):
	"""A normalization method for Copy Number Aberration in cancer samples

	Performs ratio, GC content correction and normalization of data obtained using low coverage (one read every 100-10,000 bp) high troughput sequencing. It performs a "discrete" normalization looking for the ploidy of the genome. It will also provide tumour content if at least two ploidy states can be found.
	"""
	
	homepage = "http://www.r-project.org"
	bioc = "CNAnorm"

	version("1.54.0", commit="25c46fba8ccf2270093090d58eee72543f3a2dac")
	version("1.48.0", commit="9243081606131ef0d6c96e59745df710e3a17a95")

	depends_on("r@2.10.1:", type=("build", "run"))
	depends_on("r-dnacopy", type=("build", "run"))
