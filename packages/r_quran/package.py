# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuran(RPackage):
	"""Complete Text of the Qur'an

	Full text, in data frames containing one row per verse, of the 
    Qur'an in Arabic (with and without vowels) and in English (the Yusuf Ali 
    and Saheeh International translations), formatted to be convenient for 
    text analysis.
	"""
	
	homepage = "https://github.com/andrewheiss/quRan"
	cran = "quRan" 

	version("0.1.0", md5="83b9d96b93b9f2bb6575b3e976380b05")

	depends_on("r@3:", type=("build", "run"))
