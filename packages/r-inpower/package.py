# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInpower(RPackage):
	"""An R package for computing the number of susceptibility SNPs

	An R package for computing the number of susceptibility SNPs and power of future studies
	"""
	
	bioc = "INPower"

	version("1.44.0", commit="e45ad402604da3acf3aaafcb78876c1fbdbeda38")
	version("1.38.0", commit="61d11e30173162a13941ecedc9b7a67a83067958")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
