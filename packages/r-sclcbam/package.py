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

	version("1.34.0", sha256="fe49f37029c0b0b2dd16362ba5f0b55b2d112c32efd3970032abb4d5307ad74a")

	depends_on("r@2.10:", type=("build", "run"))

