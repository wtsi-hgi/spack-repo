# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSclcbam(RPackage):
	"""Sequence data from chromosome 4 of a small-cell lung tumor

	Whole-exome sequencing data from a murine small-cell lung tumor; only contains data of chromosome 4.
	"""
	
	bioc = "SCLCBam" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/SCLCBam_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/SCLCBam/SCLCBam_1.34.0.tar.gz"]

	version("1.34.0", md5="660f11c1751b54cc942e91045884bfe6")

	depends_on("r@2.10:", type=("build", "run"))

