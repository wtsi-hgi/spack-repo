# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAmountain(RPackage):
	"""Active modules for multilayer weighted gene co-expression networks: a continuous optimization approach

	A pure data-driven gene network, weighted gene co-expression network (WGCN) could be constructed only from expression profile. Different layers in such networks may represent different time points, multiple conditions or various species. AMOUNTAIN aims to search active modules in multi-layer WGCN using a continuous optimization approach.
	"""
	
	bioc = "AMOUNTAIN" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/AMOUNTAIN_1.28.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/AMOUNTAIN/AMOUNTAIN_1.28.0.tar.gz"]

	version("1.28.0", md5="acf007b4bceaa196843cbcf221b762ba")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
