# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RThankyoustars(RPackage):
	"""Give your Dependencies Stars on GitHub!

	A tool for starring GitHub repositories.
	"""
	
	homepage = "https://github.com/ksmzn/ThankYouStars"
	cran = "ThankYouStars" 

	version("0.2.0", md5="ad27ba7f7f6ec8b440ef2fc8e36848dd")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
