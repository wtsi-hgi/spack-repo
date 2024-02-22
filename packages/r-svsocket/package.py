# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSvsocket(RPackage):
	"""'SciViews' - Socket Server

	A socket server allows to connect clients to R.
	"""
	
	homepage = "https://github.com/SciViews/svSocket"
	cran = "svSocket" 

	version("1.1.0", md5="66db5183bef1510cc06d8c2ab2c401e7")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-svmisc@0.9.68:", type=("build", "run"))
