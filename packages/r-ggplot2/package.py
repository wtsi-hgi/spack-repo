# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
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

	version("3.4.4", md5="13e7ad92c109bb07993373317e428415", url="https://cran.r-project.org/src/contrib/ggplot2_3.4.4.tar.gz")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-gtable@0.1.1:", type=("build", "run"))
	depends_on("r-isoband", type=("build", "run"))
	depends_on("r-lifecycle@1.0.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-scales@1.2:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-vctrs@0.5:", type=("build", "run"))
	depends_on("r-withr@2.5:", type=("build", "run"))
