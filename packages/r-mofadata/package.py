# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMofadata(RPackage):
	"""Data package for Multi-Omics Factor Analysis (MOFA)

	A collection of datasets to accompany the R package MOFA and illustrate running and analysing MOFA models.
	"""
	
	bioc = "MOFAdata" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/MOFAdata_1.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/MOFAdata/MOFAdata_1.18.0.tar.gz"]

	version("1.18.0", md5="23e46e209a43d7e62cfd6accc6a6fb44")

	depends_on("r@3.5:", type=("build", "run"))

	# experiment