# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSensitivity2x2xk(RPackage):
	"""Sensitivity Analysis for 2x2xk Tables in Observational Studies

	Performs exact or approximate adaptive or nonadaptive Cochran-Mantel-Haenszel-Birch tests and sensitivity analyses for one or two 2x2xk tables in observational studies.
	"""
	
	cran = "sensitivity2x2xk" 

	version("1.01", md5="d6774e35c0d146ec4ea6f2fc7e3725bb")

	depends_on("r-biasedurn", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
