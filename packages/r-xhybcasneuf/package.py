# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXhybcasneuf(RPackage):
	"""EBI/PSB cross-hybridisation study package

	Cross-hybridisation study on the ATH1 Affymetrix GeneChip
	"""
	
	bioc = "XhybCasneuf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/XhybCasneuf_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/XhybCasneuf/XhybCasneuf_1.40.0.tar.gz"]

	version("1.40.0", md5="f3e6306b5c05fb026e36e4c60656e25a")

	depends_on("r@2.4:", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-ath1121501cdf", type=("build", "run"))
	depends_on("r-tinesath1cdf", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))

	# experiment