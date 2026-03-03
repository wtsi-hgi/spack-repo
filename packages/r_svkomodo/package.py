# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSvkomodo(RPackage):
	"""'SciViews' - Functions to Interface with Komodo IDE

	R-side code to implement an R editor and IDE in Komodo IDE
  with the SciViews-K extension.
	"""
	
	homepage = "https://github.com/SciViews/svKomodo"
	cran = "svKomodo" 

	version("1.0.0", md5="f4209ce2f0f6d08be4baedb17c9be78d")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-svmisc@0.9.68:", type=("build", "run"))
