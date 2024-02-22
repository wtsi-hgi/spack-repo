# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsml(RPackage):
	"""Model Selection Based on Machine Learning (ML)

	Models evaluation based on a modified version of the recursive feature elimination algorithm. This package is designed to determine the optimal model(s) by leveraging all available features. 
	"""
	
	homepage = "https://github.com/mommy003/MSML"
	cran = "MSML" 

	version("1.0.0.0", md5="d875467d63d228fad3073bb8cac26d49")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-r2redux", type=("build", "run"))
	depends_on("r-r2roc", type=("build", "run"))
