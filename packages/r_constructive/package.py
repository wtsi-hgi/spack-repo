# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConstructive(RPackage):
	"""Display Idiomatic Code to Construct Most R Objects

	Prints code that can be used to recreate R objects. In a
    sense it is similar to 'base::dput()' or 'base::deparse()' but
    'constructive' strives to use idiomatic constructors.
	"""
	
	homepage = "https://github.com/cynkra/constructive"
	cran = "constructive" 

	version("0.3.0", md5="2b140ea9eeb5e5964c73865d80b2e350")
	version("0.2.0", md5="b51a6a8f12bfeac07ac2089507248aa9")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-diffobj", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-waldo", type=("build", "run"))
