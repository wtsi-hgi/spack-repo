# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RControl(RPackage):
	"""A Control Systems Toolbox

	Solves control systems problems relating to time/frequency response, LTI systems design and analysis, transfer function manipulations, and system conversion.
	"""
	
	cran = "control" 

	version("0.2.5", md5="b8bc163f376c26501c94a02e504ec98e")

	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
