# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClusterjudge(RPackage):
	"""Judging Quality of Clustering Methods using Mutual Information

	ClusterJudge implements the functions, examples and other software published as an algorithm by Gibbons, FD and Roth FP. The article is called "Judging the Quality of Gene Expression-Based Clustering Methods Using Gene Annotation" and it appeared in Genome Research, vol. 12, pp1574-1581 (2002). See package?ClusterJudge for an overview.
	"""
	
	bioc = "ClusterJudge" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/ClusterJudge_1.24.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/ClusterJudge/ClusterJudge_1.24.0.tar.gz"]

	version("1.24.0", md5="1f1db5b57d83f67f60de690e6f224bde")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-infotheo", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
