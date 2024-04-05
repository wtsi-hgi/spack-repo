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
	version("3.5.0", md5="81c1b4d3661e2b7d2420f1b01235ed60", url="https://cran.r-project.org/src/contrib/ggplot2_3.5.0.tar.gz")
	version("3.4.4", md5="13e7ad92c109bb07993373317e428415", url="https://cran.r-project.org/src/contrib/ggplot2_3.4.4.tar.gz")
	version("3.4.2", sha256="70230aa70a2c6f844fc41dd93e5f62af6859dfed390026ae58f223637e5283ca")
	version("3.4.0", sha256="a82f9e52f974389439765f71a8206ec26e3be30a8864d2c784d5ea8abcb0473e")
	version("3.3.6", sha256="bfcb4eb92a0fcd3fab713aca4bb25e916e05914f2540271a45522ad7e43943a9")
	version("3.3.5", sha256="b075294faf3af31b18e415f260c62d6000b218770e430484fe38819bdc3224ea")
	version("3.3.3", sha256="45c29e2348dbd195bbde1197a52db7764113e57f463fd3770fb899acc33423cc")
	version("3.2.0", sha256="31b6897fb65acb37913ff6e2bdc1b57f652360098ae3aa660abdcf54f84d73b3")
	version("3.1.1", sha256="bfde297f3b4732e7f560078f4ce131812a70877e6b5b1d41a772c394939e0c79")
	version("2.2.1", sha256="5fbc89fec3160ad14ba90bd545b151c7a2e7baad021c0ab4b950ecd6043a8314")
	version("2.1.0", sha256="f2c323ae855d6c089e3a52138aa7bc25b9fe1429b8df9eae89d28ce3c0dd3969")

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
