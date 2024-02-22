# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDismo(RPackage):
	"""Species Distribution Modeling.

	Methods for species distribution modeling, that is, predicting the
	environmental similarity of any site to that of the locations of known
	occurrences of a species."""

	cran = "dismo"

	version("1.3-14", md5="df359ee83b53c4a8953574f1a28b62ef")

	depends_on("r@3.6.3:", type=("build", "run"))
	depends_on("r-raster@3.5.21:", type=("build", "run"))
	depends_on("r-sp@1.4.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-terra@1.5.34:", type=("build", "run"))
	depends_on("openjdk@8:", type=("build", "link", "run"))
