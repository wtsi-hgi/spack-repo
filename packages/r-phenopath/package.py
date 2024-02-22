# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhenopath(RPackage):
	"""Genomic trajectories with heterogeneous genetic and environmental backgrounds

	PhenoPath infers genomic trajectories (pseudotimes) in the presence of heterogeneous genetic and environmental backgrounds and tests for interactions between them.
	"""
	
	bioc = "phenopath" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/phenopath_1.26.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/phenopath/phenopath_1.26.0.tar.gz"]

	version("1.26.0", md5="1bbbcb87efbf78aa39ee07851d27f498")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
