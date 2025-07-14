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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/methylMnM_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/methylMnM/methylMnM_1.40.0.tar.gz"]

	version("1.46.0", tag="RELEASE_3_21")
	version("1.40.0", sha256="d86ac70b1e8174ba06f3c6d4aa2e39454ae8f3605654affa3a9a71b45b377659")

	depends_on("r@2.12.1:", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
