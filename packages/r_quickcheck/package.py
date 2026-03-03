# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuickcheck(RPackage):
	"""Property Based Testing

	Property based testing, inspired by 
    the original 'QuickCheck'. This package builds on 
    the property based testing framework provided by 
    'hedgehog' and is designed to seamlessly integrate with 
    'testthat'.
	"""
	
	homepage = "https://github.com/armcn/quickcheck"
	cran = "quickcheck" 

	version("0.1.3", md5="fe69168a669af31a127ad6e1b42b6dbc")

	depends_on("r-testthat@3:", type=("build", "run"))
	depends_on("r-hedgehog", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-hms", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
