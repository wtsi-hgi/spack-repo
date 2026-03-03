# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSigclust(RPackage):
	"""Statistical Significance of Clustering

	SigClust is a statistical method for testing the
        significance of clustering results. SigClust can be applied to
        assess the statistical significance of splitting a data set
        into two clusters. For more than two clusters, SigClust can be
        used iteratively.
	"""
	
	cran = "sigclust" 

	version("1.1.0.1", md5="bd1316dcfef8be978b8bc8a0ac533ed2")

	depends_on("r@2.4:", type=("build", "run"))
