# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBasefun(RPackage):
	"""Infrastructure for Computing with Basis Functions

	Some very simple infrastructure for basis functions.
	"""
	
	homepage = "http://ctm.R-forge.R-project.org"
	cran = "basefun" 

	version("1.1-4", md5="d658210ec294c940d8ada869a7d1d7f1")

	depends_on("r-variables@1.1.0:", type=("build", "run"))
	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-polynom", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-orthopolynom", type=("build", "run"))
