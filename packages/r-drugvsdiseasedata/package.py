# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrugvsdiseasedata(RPackage):
	"""Drug versus Disease Data

	Data package which provides default disease expression profiles, clusters and annotation information for use with the DrugVsDisease package.
	"""
	
	bioc = "DrugVsDiseasedata"

	version("1.44.0", commit="54c086dc23a4c371626eb1ca0f5d439925f7a55a")
	version("1.38.0", commit="c3617920a4ea4199e9a07b2f59fe9bb5edcf8c9f")

	depends_on("r@2.10:", type=("build", "run"))

