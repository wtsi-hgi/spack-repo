# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeventygenedata(RPackage):
	"""ExpressionSets from the van't Veer and Van de Vijver breast cancer studies

	Gene expression data for the two breast cancer cohorts published by van't Veer and Van de Vijver in 2002.
	"""
	
	bioc = "seventyGeneData"

	version("1.44.0", commit="b5bc0baed56210c760e4da4374fefd9a313b5d46")
	version("1.38.2", commit="9f12dd96ee4f12cd5cc4cf71cceedb37380dffe3")

	depends_on("r@2.13:", type=("build", "run"))

