# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCowsay(RPackage):
	"""Messages, Warnings, Strings with Ascii Animals

	Allows printing of character strings as messages/warnings/etc.
    with ASCII animals, including cats, cows, frogs, chickens, ghosts,
    and more.
	"""
	
	homepage = "https://github.com/sckott/cowsay"
	cran = "cowsay" 

	version("0.9.0", md5="53bfc8c7710640ed71828b5082db6dc4")

	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-fortunes", type=("build", "run"))
	depends_on("r-rmsfact", type=("build", "run"))
