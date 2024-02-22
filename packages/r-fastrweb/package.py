# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastrweb(RPackage):
	"""Fast Interactive Framework for Web Scripting Using R

	Infrastrcture for creating rich, dynamic web content using R scripts while maintaining very fast response time.
	"""
	
	homepage = "http://www.rforge.net/FastRWeb/"
	cran = "FastRWeb" 

	version("1.2-1", md5="0b57eb24477fb3794ff26b990b1a3495")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-cairo", type=("build", "run"))
