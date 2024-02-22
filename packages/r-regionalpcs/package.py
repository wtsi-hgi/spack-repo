# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRegionalpcs(RPackage):
	"""Summarizing Regional Methylation with Regional Principal Components Analysis

	Functions to summarize DNA methylation data using regional principal components. Regional principal components are computed using principal components analysis within genomic regions to summarize the variability in methylation levels across CpGs. The number of principal components is chosen using either the Marcenko-Pasteur or Gavish-Donoho method to identify relevant signal in the data.
	"""
	
	homepage = "https://github.com/tyeulalio/regionalpcs"
	bioc = "regionalpcs" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/regionalpcs_1.0.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/regionalpcs/regionalpcs_1.0.0.tar.gz"]

	version("1.0.0", md5="37f0fc1370efacc719f72b419455096a")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-pcatools", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
