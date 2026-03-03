# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGoxygen(RPackage):
	"""In-Code Documentation for 'GAMS'

	A collection of tools which extract a model documentation from 'GAMS' code and comments. 
             In order to use the package you need to install 'pandoc' and 'pandoc-citeproc' 
             first (<https://pandoc.org/>).
	"""
	
	homepage = "https://github.com/pik-piam/goxygen"
	cran = "goxygen" 

	version("1.0.3", md5="0f6024531c26335aaf0f581f750c8c55")

	depends_on("r-pander", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-gms", type=("build", "run"))
	depends_on("r-citation", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
