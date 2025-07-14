# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCuratedbladderdata(RPackage):
	"""Bladder Cancer Gene Expression Analysis

	The curatedBladderData package provides relevant functions and data for gene expression analysis in patients with bladder cancer.
	"""
	
	homepage = "https://github.com/lima1/curatedBladderData"
	bioc = "curatedBladderData"

	version("1.44.0", commit="1a9065cbede6713565257eb6eb5c64163d6bacb6")
	version("1.38.0", commit="4d4c2f7f568a524b649c5e81e4c8458d7cb4434c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))

