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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ASSET_2.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ASSET/ASSET_2.20.0.tar.gz"]

	version("2.26.0", tag="RELEASE_3_21")
	version("2.20.0", sha256="acbbae5b669c3c11f2a8ff8ec62102781a3596b21d8426e047dfea9d4a2ca156")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-rmeta", type=("build", "run"))
