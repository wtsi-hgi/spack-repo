# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInspectchangepoint(RPackage):
	"""High-Dimensional Changepoint Estimation via Sparse Projection

	Provides a data-driven projection-based method for estimating changepoints in high-dimensional time series. Multiple changepoints are estimated using a (wild) binary segmentation scheme.
	"""
	
	cran = "InspectChangepoint" 

	version("1.2", md5="d70f7aeb958dd19a94ca58f1b42e5737")

	depends_on("r-mass", type=("build", "run"))
