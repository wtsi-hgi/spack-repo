# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModeldatatoo(RPackage):
	"""More Data Sets Useful for Modeling Examples

	More data sets used for demonstrating or testing model-related 
    packages are contained in this package. The data sets are downloaded and
    cached, allowing for more and bigger data sets.
	"""
	
	homepage = "https://github.com/tidymodels/modeldatatoo"
	cran = "modeldatatoo" 

	version("0.3.0", md5="981099a267c2890d70f019de77972bfb")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-pins", type=("build", "run"))
