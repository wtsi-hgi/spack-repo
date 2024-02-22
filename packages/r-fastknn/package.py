# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastknn(RPackage):
	"""Fast k-Nearest Neighbors

	Compute labels for a test set according to the k-Nearest Neighbors classification. This is a fast way to do k-Nearest Neighbors classification because the distance matrix -between the features of the observations- is an input to the function rather than being calculated in the function itself every time.
	"""
	
	cran = "FastKNN" 

	version("0.0.1", md5="88b551b7c936ece0991f40fefe8abfcf")

	depends_on("r-pdist", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
