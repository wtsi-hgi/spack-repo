# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYoungswimmers(RPackage):
	"""Young Swimmers Dataset

	Dataset from the young elite swimmers study.
	"""
	
	homepage = "https://github.com/NIM-ACh/youngSwimmers/"
	cran = "youngSwimmers" 

	version("0.0.1", md5="286ba94b8eeabca98de9c611303d40eb")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
