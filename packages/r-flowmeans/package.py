# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowmeans(RPackage):
	"""Non-parametric Flow Cytometry Data Gating

	Identifies cell populations in Flow Cytometry data using non-parametric clustering and segmented-regression-based change point detection. Note: R 2.11.0 or newer is required.
	"""
	
	bioc = "flowMeans" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/flowMeans_1.62.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/flowMeans/flowMeans_1.62.0.tar.gz"]

    version("1.68.0", tag="RELEASE_3_21")
	version("1.62.0", sha256="7b0962e21f4425573f70641de016e4395a45b51f42215c1aa2a3cde60a2bc31a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-rrcov", type=("build", "run"))
	depends_on("r-feature", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
