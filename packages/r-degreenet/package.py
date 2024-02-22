# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDegreenet(RPackage):
	"""Models for Skewed Count Distributions Relevant to Networks

	Likelihood-based inference for skewed count distributions, typically of degrees used in network modeling. "degreenet" is a part of the "statnet" suite of packages for network analysis. See Jones and Handcock <doi:10.1098/rspb.2003.2369>.
	"""
	
	homepage = "https://statnet.org"
	cran = "degreenet" 

	version("1.3-5", md5="9f3694a286bd7bb804b13949dcb8d567")

	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
