# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgplot2(RPackage):
	"""Create Elegant Data Visualisations Using the Grammar of Graphics.

	A system for 'declaratively' creating graphics, based on "The Grammar of
	Graphics". You provide the data, tell 'ggplot2' how to map variables to
	aesthetics, what graphical primitives to use, and it takes care of the
	details."""

	cran = "ggplot2"

	license("MIT")

	version("3.5.0", md5="81c1b4d3661e2b7d2420f1b01235ed60", url="https://cran.r-project.org/src/contrib/ggplot2_3.5.0.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-gtable@0.1.1:", type=("build", "run"))
	depends_on("r-isoband", type=("build", "run"))
	depends_on("r-lifecycle@1.0.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-scales@1.3:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-vctrs@0.5:", type=("build", "run"))
	depends_on("r-withr@2.5:", type=("build", "run"))
