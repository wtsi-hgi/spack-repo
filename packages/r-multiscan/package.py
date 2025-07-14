# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultiscan(RPackage):
	"""R package for combining multiple scans

	Estimates gene expressions from several laser scans of the same microarray
	"""
	
	bioc = "multiscan"

	version("1.68.0", commit="3e3032f5934871ce9db7044de62c28ed6a39ae20")
	version("1.62.0", commit="d7898040e578f1184715741dec5a7bedb4c6c9c1")

	depends_on("r@2.3:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
