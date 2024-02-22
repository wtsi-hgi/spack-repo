# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAmazonspr(RPackage):
	"""Get Amazon Sp Data via the 'Windsor.ai' API

	Collect  your data on digital marketing campaigns from Amazon Sp using the 'Windsor.ai' API <https://windsor.ai/api-fields/>.
	"""
	
	homepage = "https://windsor.ai/"
	cran = "amazonspR" 

	version("0.1.0", md5="2c2a26190092cb1a3fd8ff57b242ab9a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-jsonlite@1.7.2:", type=("build", "run"))
