# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTdbasedufeadv(RPackage):
	"""Advanced package of tensor decomposition based unsupervised feature extraction

	This is an advanced version of TDbasedUFE, which is a comprehensive package to perform Tensor decomposition based unsupervised feature extraction. In contrast to TDbasedUFE which can perform simple the feature selection and the multiomics analyses, this package can perform more complicated and advanced features, but they are not so popularly required. Only users who require more specific features can make use of its functionality.
	"""
	
	homepage = "https://github.com/tagtag/TDbasedUFEadv"
	bioc = "TDbasedUFEadv"

	version("1.8.1", commit="aeac24a9e67c981770e20443042c36b90f41e6c2")
	version("1.2.0", commit="266b4f5abe76d90df3c1846ca021e832f39ebece")

	depends_on("r-tdbasedufe", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-rtensor", type=("build", "run"))
	depends_on("r-rtcga", type=("build", "run"))
	depends_on("r-enrichplot", type=("build", "run"))
	depends_on("r-dose", type=("build", "run"))
	depends_on("r-stringdb", type=("build", "run"))
	depends_on("r-enrichr", type=("build", "run"))
	depends_on("r-hash", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
