# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStrex(RPackage):
	"""Extra String Manipulation Functions

	There are some things that I wish were easier with the
    'stringr' or 'stringi' packages. The foremost of these is the
    extraction of numbers from strings. 'stringr' and 'stringi' make you
    figure out the regular expression for yourself; 'strex' takes care of
    this for you. There are many other handy functionalities in 'strex'.
    Contributions to this package are encouraged; it is intended as a
    miscellany of string manipulation functions that cannot be found in
    'stringi' or 'stringr'.
	"""
	
	homepage = "https://rorynolan.github.io/strex/"
	cran = "strex" 

	version("2.0.0", md5="a044e493f751df4369925a5c967b8277")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-stringr@1.5:", type=("build", "run"))
	depends_on("r-checkmate@1.9.3:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-stringi@1.7.8:", type=("build", "run"))
