# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimico(RPackage):
	"""Set-Based Inference for Multiple Interval-Censored Outcomes

	Contains tests for association between a set of genetic variants and multiple correlated outcomes that are interval censored. Interval-censored data arises when the exact time of the onset of an outcome of interest is unknown but known to fall between two time points.
	"""
	
	cran = "SIMICO" 

	version("0.2.0", md5="1bfb4555c4cb1e3fec457419a4a532b3")

	depends_on("r-bindata", type=("build", "run"))
	depends_on("r-fastghquad", type=("build", "run"))
	depends_on("r-compquadform", type=("build", "run"))
	depends_on("r-icskat", type=("build", "run"))
