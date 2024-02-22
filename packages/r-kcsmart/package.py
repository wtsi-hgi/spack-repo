# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKcsmart(RPackage):
	"""Multi sample aCGH analysis package using kernel convolution

	Multi sample aCGH analysis package using kernel convolution
	"""
	
	bioc = "KCsmart" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/KCsmart_2.60.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/KCsmart/KCsmart_2.60.0.tar.gz"]

	version("2.60.0", md5="e50f547d912df8deb29537d5e27fc5d0")

	depends_on("r-siggenes", type=("build", "run"))
	depends_on("r-multtest", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
