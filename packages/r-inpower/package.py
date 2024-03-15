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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/INPower_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/INPower/INPower_1.38.0.tar.gz"]

	version("1.38.0", md5="3b769c08ded506c713da036c30fe4da9")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
