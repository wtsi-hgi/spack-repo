# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetagxbreast(RPackage):
	"""Transcriptomic Breast Cancer Datasets

	A collection of Breast Cancer Transcriptomic Datasets that are part of the MetaGxData package compendium.
	"""
	
	bioc = "MetaGxBreast" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/MetaGxBreast_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/MetaGxBreast/MetaGxBreast_1.22.0.tar.gz"]

	version("1.22.0", md5="e711302482bca1429de5fe2e5276c788")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))

	# experiment