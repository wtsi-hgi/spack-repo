# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMethylmnm(RPackage):
	"""detect different methylation level (DMR)

	To give the exactly p-value and q-value of MeDIP-seq and MRE-seq data for different samples comparation.
	"""
	
	bioc = "methylMnM" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/methylMnM_1.40.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/methylMnM/methylMnM_1.40.0.tar.gz"]

	version("1.40.0", md5="3d6c83c4fa30daea5b1c91e70f67c6b5")

	depends_on("r@2.12.1:", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
