# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJsonify(RPackage):
	"""Convert Between 'R' Objects and Javascript Object Notation
	(JSON).

	Conversions between 'R' objects and Javascript Object Notation (JSON) using
	the 'rapidjsonr' library
	<https://CRAN.R-project.org/package=rapidjsonr>."""

	cran = "jsonify"

	license("MIT")

	version("1.2.2", md5="f1886cbb9d6978fea91124f4d58526a4")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rapidjsonr@1.2:", type=("build", "run"))
