# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProteinprofiles(RPackage):
	"""Protein Profiling

	Significance assessment for distance measures of time-course protein profiles
	"""
	
	bioc = "proteinProfiles"

	version("1.48.0", commit="76098c8a8b51c9512f8b1e2abc3ed1c214efbb57")
	version("1.42.0", commit="7b9a480648bd0121fec40628268f56287effd651")

	depends_on("r@2.15.2:", type=("build", "run"))
