# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArrow(RPackage):
	"""Integration to 'Apache' 'Arrow'

	'Apache' 'Arrow' <https://arrow.apache.org/> is a cross-language
    development platform for in-memory data. It specifies a standardized
    language-independent columnar memory format for flat and hierarchical data,
    organized for efficient analytic operations on modern hardware. This
    package provides an interface to the 'Arrow C++' library.
	"""
	
	homepage = "https://github.com/apache/arrow/"
	cran = "arrow" 

	version("14.0.0.2", md5="84cefe34da6af43984b308ca2a57d7bd")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-bit64@0.9.7:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-tidyselect@1:", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-cpp11@0.4.2:", type=("build", "run"))
	depends_on("curl", type=("build", "link", "run"))
