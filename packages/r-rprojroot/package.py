# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRprojroot(RPackage):
	"""Finding Files in Project Subdirectories.

	Robust, reliable and flexible paths to files below a project root.  The
	'root' of a project is defined as a directory that matches a certain
	criterion, e.g., it contains a certain regular file."""

	cran = "rprojroot"

	version("2.0.4", md5="4cbcf2cb74cbb76a6065182adf01b051")

	depends_on("r@3:", type=("build", "run"))
