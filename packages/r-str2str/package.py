# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStr2str(RPackage):
	"""Convert R Objects from One Structure to Another

	Offers a suite of functions for converting to and from
    (atomic) vectors, matrices, data.frames, and (3D+) arrays as well
    as lists of these objects. It is an alternative to the base R
    as.<str>.<method>() functions (e.g., as.data.frame.array()) that
    provides more useful and/or flexible restructuring of R objects.
    To do so, it only works with common structuring of R objects (e.g.,
    data.frames with only atomic vector columns).
	"""
	
	cran = "str2str" 

	version("1.0.0", md5="5e61a16941360b12e06ddb5562ac79a5")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
