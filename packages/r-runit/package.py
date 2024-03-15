# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRunit(RPackage):
	"""R Unit Test Framework.

	R functions implementing a standard Unit Testing framework, with additional
	code inspection and report generation tools."""

	cran = "RUnit"

	license("GPL-2.0-only")

	version("0.4.33", md5="15fe8bcba8961e79e9a43df943f82467")

	depends_on("r@2.5:", type=("build", "run"))
