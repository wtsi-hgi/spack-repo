# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYesno(RPackage):
	"""Ask Yes-No Questions

	Asks Yes-No questions with variable or custom responses.
	"""
	
	homepage = "https://github.com/poissonconsulting/yesno"
	cran = "yesno" 

	version("0.1.2", md5="2b35fba2de07f303fc5eecdb0eb69ee6")

	depends_on("r@3.3:", type=("build", "run"))
