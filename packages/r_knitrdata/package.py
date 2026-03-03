# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKnitrdata(RPackage):
	"""Data Language Engine for 'knitr' / 'rmarkdown'

	Implements a data language engine for incorporating data directly in 
    'rmarkdown' documents so that they can be made completely standalone.
	"""
	
	homepage = "https://github.com/dmkaplan2000/knitrdata"
	cran = "knitrdata" 

	version("0.6.1", md5="44d674ae50e092a17e76bfc0c7bf39cf")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-xfun@0.16:", type=("build", "run"))
