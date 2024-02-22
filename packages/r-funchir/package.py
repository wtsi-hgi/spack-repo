# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFunchir(RPackage):
	"""Convenience Functions by Michael Chirico

	YACFP (Yet Another Convenience Function Package). get_age() is a fast & accurate tool for measuring fractional years between two dates. abbr_to_colClass() is a much more concise way of feeding many types to a colClass argument in a data reader. stale_package_check() tries to identify any library() calls to unused packages.
	"""
	
	homepage = "https://github.com/MichaelChirico/funchir"
	cran = "funchir" 

	version("0.2.2", md5="2f9e58f844be2407b9b9955e31ef3563")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
