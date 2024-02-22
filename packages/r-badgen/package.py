# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBadgen(RPackage):
	"""Fast and Simple Badge Generator

	Bindings to 'badgen' <https://www.npmjs.com/package/badgen> to
    generate beautiful 'svg' badges in R without internet access. Images can
    be converted to 'png' using the 'rsvg' package as shown in examples.
	"""
	
	homepage = "https://github.com/jeroen/badgen/"
	cran = "badgen" 

	version("1.0.0", md5="0bbf01144b7bd16107256f1ceee06cc4")

	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-v8", type=("build", "run"))
