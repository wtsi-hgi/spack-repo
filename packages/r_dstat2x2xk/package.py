# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDstat2x2xk(RPackage):
	"""Demonstrated Insensitivity to Bias in 2x2xK Contingency Tables

	For an observational study with binary treatment, binary outcome and K strata, implements a d-statistic that uses those strata most insensitive to unmeasured bias in treatment assignment.<doi:10.1093/biomet/asaa032>  The package has one function, dstat2x2xk.
	"""
	
	cran = "dstat2x2xk" 

	version("0.2.0", md5="ce18acb14abbd1d7655ba47873c0854a")

	depends_on("r-biasedurn", type=("build", "run"))
