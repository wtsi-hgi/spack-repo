# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRflexscan(RPackage):
	"""The Flexible Spatial Scan Statistic

	Functions for the detection of spatial clusters using the flexible
    spatial scan statistic developed by Tango and Takahashi (2005) <doi:10.1186/1476-072X-4-11>.
    This package implements a wrapper for the C routine used in the FleXScan 3.1.2 
    <https://sites.google.com/site/flexscansoftware/home> developed by Takahashi,
    Yokoyama, and Tango. For details, see Otani et al. (2021) <doi:10.18637/jss.v099.i13>.
	"""
	
	homepage = "https://tkhrotn.github.io/rflexscan/"
	cran = "rflexscan" 

	version("1.1.0", md5="3607a01771dc7deba86301fdd262d355")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
