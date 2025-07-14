# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChromstardata(RPackage):
	"""ChIP-seq data for Demonstration Purposes

	ChIP-seq data for demonstration purposes in the chromstaR package.
	"""
	
	bioc = "chromstaRData"

	version("1.34.0", commit="3fce4155738df3dc7e03fd7c9b2ce8233b5df0b0")
	version("1.28.0", commit="0ec080ab9c51e2a788dc7294de30490b772e8607")

	depends_on("r@3.3:", type=("build", "run"))

