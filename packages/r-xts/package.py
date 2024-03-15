# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXts(RPackage):
	"""eXtensible Time Series.

	Provide for uniform handling of R's different time-based data classes by
	extending zoo, maximizing native format information preservation and
	allowing for user level customization and extension, while simplifying
	cross-class interoperability."""

	cran = "xts"

	license("GPL-2.0-or-later")

	version("0.13.2", md5="58945668fa13f12e2efd18d327c422e4")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
