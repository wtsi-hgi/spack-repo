# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHealthyflowdata(RPackage):
	"""Healthy dataset used by the flowMatch package

	A healthy dataset with 20 flow cytometry samples used by the flowMatch package.
	"""
	
	bioc = "healthyFlowData"

	version("1.46.0", commit="fb9c2498b15619fde8fb931f92234ed843f332fb")
	version("1.40.0", commit="c2360e951cdbefaefdaf0007155569d7d86d8d45")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))

