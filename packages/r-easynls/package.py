# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REasynls(RPackage):
	"""Easy Nonlinear Model

	Fit and plot some nonlinear models.
	"""
	
	cran = "easynls" 

	version("5.0", md5="0a79fb09f006ea5071118197264f03b6")

	depends_on("r@3:", type=("build", "run"))
