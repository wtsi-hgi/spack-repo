# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnbeadsHg19(RPackage):
	"""RnBeads.hg19

	Automatically generated RnBeads annotation package for the assembly hg19.
	"""
	
	bioc = "RnBeads.hg19"

	version("1.40.0", commit="f7ea44bf70d3368ab289ab38e2ca83fb45f45b14")
	version("1.34.0", commit="4d3f651a201f9e97c91f3ea4978605a2cd7abf4c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))

