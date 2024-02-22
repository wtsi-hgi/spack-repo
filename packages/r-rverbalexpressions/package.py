# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRverbalexpressions(RPackage):
	"""Create Regular Expressions Easily

	Build regular expressions using grammar and functionality inspired 
    by <https://github.com/VerbalExpressions>. Usage of the %>% is encouraged to
    build expressions in a chain-like fashion.
	"""
	
	homepage = "https://github.com/tyluRp/RVerbalExpressions"
	cran = "RVerbalExpressions" 

	version("0.1.0", md5="451182ae27f889fd81f6de4f1c37c949")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
