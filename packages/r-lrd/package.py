# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLrd(RPackage):
	"""A Package for Processing Lexical Response Data

	Lexical response data is a package that 
    can be used for processing cued-recall, free-recall, 
    and sentence responses from memory experiments.
	"""
	
	homepage = "https://npm27.github.io/lrd/"
	cran = "lrd" 

	version("0.1.0", md5="437cd3520f81653a677446e79301a197")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
