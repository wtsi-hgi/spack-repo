# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMakedummies(RPackage):
	"""Create Dummy Variables from Categorical Data

	Create dummy variables from categorical data.
    This package can convert categorical data (factor and ordered) into
    dummy variables and handle multiple columns simultaneously.
    This package enables to select whether a dummy variable for base group
    is included (for principal component analysis/factor analysis) or
    excluded (for regression analysis) by an option.
    'makedummies' function accepts 'data.frame', 'matrix', and
    'tbl' (tibble) class (by 'tibble' package).
    'matrix' class data is automatically converted to 'data.frame' class.
	"""
	
	homepage = "https://github.com/toshi-ara/makedummies"
	cran = "makedummies" 

	version("1.2.1", md5="94a3dff9b9dd6416751b78be280512a2")

	depends_on("r-tibble", type=("build", "run"))
