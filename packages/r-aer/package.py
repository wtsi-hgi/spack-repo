# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAer(RPackage):
	"""Applied Econometrics with R.

	Functions, data sets, examples, demos, and vignettes for the book Christian
	Kleiber and Achim Zeileis (2008), Applied Econometrics with R,
	Springer-Verlag, New York.  ISBN 978-0-387-77316-2."""

	cran = "AER"

	version("1.2-12", md5="89bb4ea783447c20c9b2c37ed2ed9cdb")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-car@2.0.19:", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-sandwich@2.4.0:", type=("build", "run"))
	depends_on("r-survival@2.37.5:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-formula@0.2.0:", type=("build", "run"))
