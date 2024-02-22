# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAsset(RPackage):
	"""An R package for subset-based association analysis of heterogeneous traits and subtypes

	An R package for subset-based analysis of heterogeneous traits and disease subtypes. The package allows the user to search through all possible subsets of z-scores to identify the subset of traits giving the best meta-analyzed z-score. Further, it returns a p-value adjusting for the multiple-testing involved in the search. It also allows for searching for the best combination of disease subtypes associated with each variant.
	"""
	
	bioc = "ASSET" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/ASSET_2.20.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/ASSET/ASSET_2.20.0.tar.gz"]

	version("2.20.0", md5="395bcc1b0256acc248c5d3440bf5dfeb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-rmeta", type=("build", "run"))
