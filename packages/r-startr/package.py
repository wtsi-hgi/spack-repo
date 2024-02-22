# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStartr(RPackage):
	"""Automatically Retrieve Multidimensional Distributed Data Sets

	Tool to automatically fetch, transform and arrange subsets of
    multi- dimensional data sets (collections of files) stored in local and/or
    remote file systems or servers, using multicore capabilities where possible.
    The tool provides an interface to perceive a collection of data sets as a single
    large multidimensional data array, and enables the user to request for automatic
    retrieval, processing and arrangement of subsets of the large array. Wrapper
    functions to add support for custom file formats can be plugged in/out, making
    the tool suitable for any research field where large multidimensional data sets
    are involved.
	"""
	
	homepage = "https://earth.bsc.es/gitlab/es/startR/"
	cran = "startR" 

	version("2.3.1", md5="a20d438085c7f100818156d5894f1eeb")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-bigmemory", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-multiapply@2.1:", type=("build", "run"))
	depends_on("r-easyncdf", type=("build", "run"))
	depends_on("r-s2dv", type=("build", "run"))
	depends_on("r-climprojdiags", type=("build", "run"))
	depends_on("r-pcict", type=("build", "run"))
