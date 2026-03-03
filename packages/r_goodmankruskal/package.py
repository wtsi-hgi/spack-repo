# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGoodmankruskal(RPackage):
	"""Association Analysis for Categorical Variables

	Association analysis between categorical
    variables using the Goodman and Kruskal tau measure. This asymmetric association
    measure allows the detection of asymmetric relations between categorical
    variables (e.g., one variable obtained by re-grouping another).
	"""
	
	cran = "GoodmanKruskal" 

	version("0.0.3", md5="f2b66c5b75bcbfec1a196aa792709e1a")

	depends_on("r@3.2.4:", type=("build", "run"))
	depends_on("r-classint", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
