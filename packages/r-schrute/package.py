# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSchrute(RPackage):
	"""The Entire Transcript from the Office in Tidy Format

	The complete scripts from the American version of the Office
    television show in tibble format. Use this package to analyze and have
    fun with text from the best series of all time.
	"""
	
	homepage = "https://github.com/bradlindblad/schrute"
	cran = "schrute" 

	version("1.0.1", md5="90c69f3cb98ce06c41b71b7cac46c506")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
