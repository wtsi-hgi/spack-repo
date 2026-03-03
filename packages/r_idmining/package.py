# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdmining(RPackage):
	"""Intrinsic Dimension for Data Mining

	Contains techniques for mining large and high-dimensional data
    sets by using the concept of Intrinsic Dimension (ID). Here the ID is
    not necessarily an integer. It is extended to fractal dimensions. And
    the Morisita estimator is used for the ID estimation, but other
    tools are included as well.
	"""
	
	homepage = "https://www.sites.google.com/site/jeangolayresearch/"
	cran = "IDmining" 

	version("1.0.7", md5="22e2d094c82eb35e638cf712962491a7")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
