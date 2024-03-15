# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTinytex(RPackage):
	"""Helper Functions to Install and Maintain TeX Live, and Compile LaTeX
	Documents.

	Helper functions to install and maintain the 'LaTeX' distribution named
	'TinyTeX' (<https://yihui.name/tinytex/>), a lightweight, cross-platform,
	portable, and easy-to-maintain version of 'TeX Live'. This package also
	contains helper functions to compile 'LaTeX' documents, and install missing
	'LaTeX' packages automatically."""

	cran = "tinytex"

	license("MIT")

	version("0.49", md5="0e44e8589e71a5257ddac72c5113e440")

	depends_on("r-xfun@0.29:", type=("build", "run"))
