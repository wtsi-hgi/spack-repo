# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArrays(RPackage):
	"""Using Bioconductor for Microarray Analysis

	Using Bioconductor for Microarray Analysis workflow
	"""
	
	bioc = "arrays"

	version("1.34.0", commit="aabda1d228baa37347fc5eb4cef1416f4ea5ca47")
	version("1.28.0", commit="eabeb85adc289bcebd42be1df2c79dacc1ccd8e6")

	depends_on("r@3:", type=("build", "run"))

