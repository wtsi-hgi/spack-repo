# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTypes(RPackage):
	"""Type Annotations

	Provides a simple type annotation for R that is usable in scripts,
    in the R console and in packages. It is intended as a convention to allow other
    packages to use the type information to provide error checking,
    automatic documentation or optimizations.
	"""
	
	cran = "types" 

	version("1.0.0", md5="0085947dff87ab2ff30a4ac5e55eb2c4")

	depends_on("r@3.0.3:", type=("build", "run"))
