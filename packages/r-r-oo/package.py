# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RROo(RPackage):
	"""R Object-Oriented Programming with or without References.

	Methods and classes for object-oriented programming in R with or without
	references. Large effort has been made on making definition of methods as
	simple as possible with a minimum of maintenance for package developers.
	The package has been developed since 2001 and is now considered very
	stable. This is a cross-platform package implemented in pure R that defines
	standard S3 classes without any tricks."""

	cran = "R.oo"

	version("1.26.0", md5="7575e8599deb1b6387dd50a85364c3b7")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-r-methodss3@1.8.2:", type=("build", "run"))
