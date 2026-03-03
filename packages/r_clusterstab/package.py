# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClusterstab(RPackage):
	"""Compute cluster stability scores for microarray data

	This package can be used to estimate the number of clusters in a set of microarray data, as well as test the stability of these clusters.
	"""
	
	bioc = "clusterStab" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/clusterStab_1.74.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/clusterStab/clusterStab_1.74.0.tar.gz"]

	version("1.74.0", md5="87f3941fd121e6a60acdefd9a682ba9a")

	depends_on("r-biobase@1.4.22:", type=("build", "run"))
	depends_on("r@1.9:", type=("build", "run"))
