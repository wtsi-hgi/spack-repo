# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChicData(RPackage):
	"""ChIC package data

	This package contains annotation and metagene profile data for the ChIC package.
	"""
	
	bioc = "ChIC.data"

	version("1.22.0", commit="0cc523ec20c165a06313c9aace1628f51faea696")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomeintervals", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-caret@6.0.78:", type=("build", "run"))

