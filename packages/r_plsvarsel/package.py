# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlsvarsel(RPackage):
	"""Variable Selection in Partial Least Squares

	Interfaces and methods for variable selection in Partial Least
    Squares. The methods include filter methods, wrapper methods and embedded
    methods. Both regression and classification is supported.
	"""
	
	homepage = "https://github.com/khliland/plsVarSel/"
	cran = "plsVarSel" 

	version("0.9.10", md5="1631b41f7a50608119319dfe1f2263a4")

	depends_on("r-pls", type=("build", "run"))
	depends_on("r-genalg", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-bdsmatrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-msqc", type=("build", "run"))
	depends_on("r-praznik", type=("build", "run"))
