# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStringmagic(RPackage):
	"""Character String Operations and Interpolation, Magic Edition

	Performs complex string operations compactly and efficiently. Supports string interpolation jointly with over 50 string operations. Also enhances regular string functions (like grep() and co). See an introduction at <https://lrberge.github.io/stringmagic/>.
	"""
	
	homepage = "https://lrberge.github.io/stringmagic/"
	cran = "stringmagic" 

	version("1.1.0", md5="dc71f4f3d14034bf20fc380d32969c4c")
	version("1.0.0", md5="fb2a47a42735f26602831e0ac3bf0997")

	depends_on("r-rcpp", type=("build", "run"))
