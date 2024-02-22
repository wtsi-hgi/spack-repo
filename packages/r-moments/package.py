# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMoments(RPackage):
	"""Moments, Cumulants, Skewness, Kurtosis and Related Tests

	Functions to calculate: moments, Pearson's kurtosis,
        Geary's kurtosis and skewness; tests related to them
        (Anscombe-Glynn, D'Agostino, Bonett-Seier).
	"""
	
	homepage = "https://www.r-project.org"
	cran = "moments" 

	version("0.14.1", md5="622afd35702c45ad010c106af2457458")

