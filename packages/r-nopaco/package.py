# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNopaco(RPackage):
	"""Non-Parametric Concordance Coefficient

	A non-parametric test for multi-observer concordance and
    differences between concordances in (un)balanced data.
	"""
	
	cran = "nopaco" 

	version("1.0.7", md5="9936af96254e38b312946dbcb30888e7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix@1.1.5:", type=("build", "run"))
