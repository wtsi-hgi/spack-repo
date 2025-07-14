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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/KCsmart_2.60.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/KCsmart/KCsmart_2.60.0.tar.gz"]

	version("2.66.0", tag="RELEASE_3_21")
	version("2.60.0", sha256="79f1116c49d0ff9eb12fd3e6ccb68e2378a6924f8ba5740be6fb0ec0883d3220")

	depends_on("r-siggenes", type=("build", "run"))
	depends_on("r-multtest", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
