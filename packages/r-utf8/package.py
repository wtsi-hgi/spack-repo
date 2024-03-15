# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUtf8(RPackage):
	"""Unicode Text Processing.

	Process and print 'UTF-8' encoded international text (Unicode). Input,
	validate, normalize, encode, format, and display."""

	cran = "utf8"

	license("Apache-2.0 OR custom")

	version("1.2.4", md5="b12b4a8b7c9fc8429a0c0633c59c7c18", url="https://cran.r-project.org/src/contrib/utf8_1.2.4.tar.gz")

	depends_on("r@2.10:", type=("build", "run"))
