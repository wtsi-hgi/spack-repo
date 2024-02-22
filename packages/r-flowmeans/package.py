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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/flowMeans_1.62.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/flowMeans/flowMeans_1.62.0.tar.gz"]

	version("1.62.0", md5="5cbb796502f09bf65cae60e4f0f53c1f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-rrcov", type=("build", "run"))
	depends_on("r-feature", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
