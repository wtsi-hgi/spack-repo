# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDamiann(RPackage):
	"""Neural Network Numerai

	Interactively train neural networks on Numerai, <https://numer.ai/>, data. Generate tournament predictions and write them to a CSV.
	"""
	
	cran = "DamiaNN" 

	version("1.0.0", md5="793b1df2f25f271b081b0e35e62d7370")

	depends_on("r-caret", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
