# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaskbad(RPackage):
	"""Masking probes with binding affinity differences

	Package includes functions to analyze and mask microarray expression data.
	"""
	
	bioc = "maskBAD"

	version("1.52.0", commit="55b30996eee1866fd559ce9d1694d63b08dd085e")
	version("1.46.0", commit="b0b9d7e357ca460c6350dca3c530beecf605c17c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-gcrma@2.27.1:", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
