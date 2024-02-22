# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlue(RPackage):
	"""Interpreted String Literals.

	An implementation of interpreted string literals, inspired by Python's
	Literal String Interpolation <https://www.python.org/dev/peps/pep-0498/>
	and Docstrings <https://www.python.org/dev/peps/pep-0257/> and Julia's
	Triple-Quoted String Literals <https://docs.julialang.org/en/stable/
	manual/strings/#triple-quoted-string-literals>."""

	cran = "glue"

	version("1.7.0", md5="e4e7b07da0c02b008d9a9759b2acbc99")

	depends_on("r@3.6:", type=("build", "run"))
