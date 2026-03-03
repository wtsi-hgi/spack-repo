# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTau(RPackage):
	"""Text Analysis Utilities

	Utilities for text analysis.
	"""
	
	cran = "tau" 

	version("0.0-25", md5="daf5cdc346cd562013b75671331375dc")

	depends_on("r@2.10:", type=("build", "run"))
