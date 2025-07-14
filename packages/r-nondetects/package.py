# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNondetects(RPackage):
	"""Non-detects in qPCR data

	Methods to model and impute non-detects in the results of qPCR experiments.
	"""
	
	bioc = "nondetects"

	version("2.38.1", commit="f01e6d6679f60333b6784b58326e9e5e59a82019")
	version("2.32.0", commit="326a610f6125519428dcc67c2378c8b895f20fda")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-biobase@2.22:", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-arm", type=("build", "run"))
	depends_on("r-htqpcr@1.16:", type=("build", "run"))
