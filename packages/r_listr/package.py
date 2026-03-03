# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RListr(RPackage):
	"""Tools for Lists

	Tools for common operations on lists. Provided are short-cuts to
    operations like selecting and merging data stored in lists. The functions in
    this package are designed to be used with pipes.
	"""
	
	cran = "listr" 

	version("0.1.0", md5="c59a38b761ad6ca9dd010f813636a164")

	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
