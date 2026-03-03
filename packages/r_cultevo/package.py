# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCultevo(RPackage):
	"""Tools, Measures and Statistical Tests for Cultural Evolution

	Provides tools for measuring the compositionality of signalling systems (in particular the information-theoretic measure due to Spike (2016) <http://hdl.handle.net/1842/25930> and the Mantel test for distance matrix correlation (after Dietz 1983) <doi:10.1093/sysbio/32.1.21>), functions for computing string and meaning distance matrices as well as an implementation of the Page test for monotonicity of ranks (Page 1963) <doi:10.1080/01621459.1963.10500843> with exact p-values up to k = 22.
	"""
	
	homepage = "https://kevinstadler.github.io/cultevo/"
	cran = "cultevo" 

	version("1.0.2", md5="7e961472c95dc63acb43f9e56014f3d7")

	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-pspearman", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
