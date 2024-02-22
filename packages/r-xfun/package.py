# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXfun(RPackage):
	"""Supporting Functions for Packages Maintained by 'Yihui Xie'.

	Miscellaneous functions commonly used in other packages maintained by
	'Yihui Xie'."""

	cran = "xfun"

	version("0.42", md5="8435824d449ee92b4ee5d74643fffe33")

