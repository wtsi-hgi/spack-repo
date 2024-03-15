# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCaracas(RPackage):
	"""Computer Algebra.

	Computer algebra via the 'SymPy' library (<https://www.sympy.org/>). This
	makes it possible to solve equations symbolically, find symbolic integrals,
	symbolic sums and other important quantities."""

	cran = "caracas"

	license("GPL-2.0-or-later")

	version("2.1.1", md5="772690703f3c912462ed6c78804e485e")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-reticulate@1.14:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-doby@4.6.15:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("python", type=("build", "link", "run"))
