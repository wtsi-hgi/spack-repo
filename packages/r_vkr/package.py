# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVkr(RPackage):
	"""Access to VK API via R

	Provides an interface to the VK API <https://vk.com/dev/methods>.
      VK <https://vk.com/> is the largest European online social networking
      service, based in Russia.
	"""
	
	homepage = "https://github.com/Dementiy/vkR"
	cran = "vkR" 

	version("0.2", md5="94267013ea927b02f4067d0e59dc010a")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
