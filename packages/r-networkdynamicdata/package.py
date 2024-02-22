# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetworkdynamicdata(RPackage):
	"""Dynamic (Longitudinal) Network Datasets

	A collection of dynamic network data sets from various sources and multiple authors represented as 'networkDynamic'-formatted objects.
	"""
	
	homepage = "http://statnet.org"
	cran = "networkDynamicData" 

	version("0.2.1", md5="19876e2b8f1469a31cbc7581141cc414")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-networkdynamic@0.6:", type=("build", "run"))
	depends_on("r-network@1.9:", type=("build", "run"))
