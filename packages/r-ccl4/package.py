# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCcl4(RPackage):
	"""Carbon Tetrachloride (CCl4) treated hepatocytes

	NChannelSet for rat hepatocytes treated with Carbon Tetrachloride (CCl4) data from LGC company.
	"""
	
	bioc = "CCl4"

	version("1.46.0", commit="242cf8777b60f52ef110a58e370b3aec15b17f0f")
	version("1.40.0", commit="b7d89b9d38b5d8945386cd99ebe379e383d0f6eb")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))

