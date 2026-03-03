# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFreshd(RPackage):
	"""Fast Robust Estimation of Signals in Heterogeneous Data

	Procedure for solving the maximin problem for identical design across heterogeneous data groups. Particularly efficient when the design matrix is either orthogonal or has tensor structure. Orthogonal wavelets can be specified for 1d, 2d or 3d data simply by name. For tensor structured design the tensor components (two or three) may be supplied. The package also provides an efficient implementation of the generic magging estimator.
	"""
	
	cran = "FRESHD" 

	version("1.0", md5="3805bac73d8ef18fedf5407dd020cc7c")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-glamlasso", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
