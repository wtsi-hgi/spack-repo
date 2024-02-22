# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTbm(RPackage):
	"""Transformation Boosting Machines

	Boosting the likelihood of conditional and shift transformation models as introduced in doi{10.1007/s11222-019-09870-4}.
	"""
	
	homepage = "http://ctm.R-forge.R-project.org"
	cran = "tbm" 

	version("0.3-5", md5="7353d3f2db3da5865cec08aeecaa13ab")

	depends_on("r-mlt@1.0.6:", type=("build", "run"))
	depends_on("r-mboost@2.8.2:", type=("build", "run"))
	depends_on("r-variables", type=("build", "run"))
	depends_on("r-basefun", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-coneproj", type=("build", "run"))
