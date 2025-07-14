# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnbeadsMm9(RPackage):
	"""RnBeads.mm9

	Automatically generated RnBeads annotation package for the assembly mm9.
	"""
	
	bioc = "RnBeads.mm9"

	version("1.40.0", commit="c515f023c36b15950e1cf18a4d9f6b278f113f0e")
	version("1.34.0", commit="e3e45c713cd617fdacb3998c333f71ab6a529b03")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))

