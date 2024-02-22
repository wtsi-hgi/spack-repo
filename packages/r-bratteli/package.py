# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBratteli(RPackage):
	"""Deal with Bratteli Graphs

	Utilities for Bratteli graphs. A tree is an example of a Bratteli
    graph. The package provides a function which generates a 'LaTeX' file
    that renders the given Bratteli graph. It also provides functions to
    compute the dimensions of the vertices, the intrinsic kernels and the
    intrinsic distances. Intrinsic kernels and distances were introduced
    by Vershik (2014) <doi:10.1007/s10958-014-1958-0>.
	"""
	
	homepage = "https://github.com/stla/bratteliR"
	cran = "bratteli" 

	version("1.0.0", md5="e239d78f166d39517f0fcbf470765193")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-diagram", type=("build", "run"))
	depends_on("r-gmp", type=("build", "run"))
	depends_on("r-kantorovich", type=("build", "run"))
