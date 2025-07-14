# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTofsimsdata(RPackage):
	"""Import, process and analysis of ToF-SIMS imaging data

	This packages contains data to be used with the 'tofsims' package.
	"""
	
	bioc = "tofsimsData"

	version("1.36.0", commit="6433badf6aba1319a2ae0c67399310ec0af2e271")
	version("1.30.0", commit="cb3768dc1177ffcb5345642acd30437b84eb6721")

	depends_on("r@3.2:", type=("build", "run"))

