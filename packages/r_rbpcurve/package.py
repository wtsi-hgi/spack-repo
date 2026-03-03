# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbpcurve(RPackage):
	"""The Residual-Based Predictiveness Curve

	The RBP curve is a visual tool to assess the
    performance of prediction models.
	"""
	
	homepage = "https://github.com/giuseppec/RBPcurve"
	cran = "RBPcurve" 

	version("1.2", md5="3aa6a3c1b49117e3125e77cb86fdbb5d")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-mlr@2.11:", type=("build", "run"))
	depends_on("r-bbmisc@1.11:", type=("build", "run"))
	depends_on("r-checkmate@1.8.2:", type=("build", "run"))
	depends_on("r-shape", type=("build", "run"))
	depends_on("r-teachingdemos", type=("build", "run"))
