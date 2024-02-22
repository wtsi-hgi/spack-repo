# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQualv(RPackage):
	"""Qualitative Validation Methods

	Qualitative methods for the validation of dynamic models.
    It contains (i) an orthogonal set of deviance measures for absolute,
    relative and ordinal scale and (ii) approaches accounting for time
    shifts. The first approach transforms time to take time delays and speed
    differences into account. The second divides the time series into
    interval units according to their main features and finds the longest
    common subsequence (LCS) using a dynamic programming algorithm.
	"""
	
	homepage = "http://qualV.R-Forge.R-Project.org/"
	cran = "qualV" 

	version("0.3-5", md5="f10824912626d65fc1fe53fbccc40807")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
