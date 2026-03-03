# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTibblify(RPackage):
	"""Rectangle Nested Lists

	A tool to rectangle a nested list, that is to convert it into
    a tibble. This is done automatically or according to a given
    specification.  A common use case is for nested lists coming from
    parsing JSON files or the JSON response of REST APIs. It is supported
    by the 'vctrs' package and therefore offers a wide support of vector
    types.
	"""
	
	homepage = "https://github.com/mgirlich/tibblify"
	cran = "tibblify" 

	version("0.3.1", md5="ed7ded91a15682290f02352a906c9af9")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cli@3.6.2:", type=("build", "run"))
	depends_on("r-lifecycle@1.0.4:", type=("build", "run"))
	depends_on("r-purrr@1.0.2:", type=("build", "run"))
	depends_on("r-rlang@1.1.3:", type=("build", "run"))
	depends_on("r-tibble@3.2.1:", type=("build", "run"))
	depends_on("r-tidyselect@1.2:", type=("build", "run"))
	depends_on("r-vctrs@0.6.5:", type=("build", "run"))
	depends_on("r-withr@2.5.2:", type=("build", "run"))
