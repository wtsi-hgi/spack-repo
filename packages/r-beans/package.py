# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBeans(RPackage):
	"""Data on Dried Beans

	These data contain morphological image measurements for dried
    beans from Koklu and Ozkan (2020) <doi:10.1016/j.compag.2020.105507>.
	"""
	
	cran = "beans" 

	version("0.1.0", md5="89718121482c3bc76b3d8e68dcc153d8")

	depends_on("r@2.10:", type=("build", "run"))
