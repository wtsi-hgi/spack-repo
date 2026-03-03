# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REdfun(RPackage):
	"""Creating Empirical Distribution Functions

	Easily creating empirical distribution functions from data: 'dfun', 'pfun',
    'qfun' and 'rfun'.
	"""
	
	homepage = "https://cran.r-project.org/package=edfun"
	cran = "edfun" 

	version("0.2.0", md5="a442c5ed86b7454055222ecb619b7fca")

	depends_on("r@3:", type=("build", "run"))
