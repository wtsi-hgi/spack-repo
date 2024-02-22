# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTestthat(RPackage):
	"""Unit Testing for R.

	Software testing is important, but, in part because it is frustrating and
	boring, many of us avoid it. 'testthat' is a testing framework for R that
	is easy to learn and use, and integrates with your existing 'workflow'."""

	cran = "testthat"

	version("3.2.1", md5="cb9ddcf70c6b030743c9685e0f104f67")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-brio@1.1.3:", type=("build", "run"))
	depends_on("r-callr@3.7.3:", type=("build", "run"))
	depends_on("r-cli@3.6.1:", type=("build", "run"))
	depends_on("r-desc@1.4.2:", type=("build", "run"))
	depends_on("r-digest@0.6.33:", type=("build", "run"))
	depends_on("r-evaluate@0.21:", type=("build", "run"))
	depends_on("r-jsonlite@1.8.7:", type=("build", "run"))
	depends_on("r-lifecycle@1.0.3:", type=("build", "run"))
	depends_on("r-magrittr@2.0.3:", type=("build", "run"))
	depends_on("r-pkgload@1.3.2.1:", type=("build", "run"))
	depends_on("r-praise@1:", type=("build", "run"))
	depends_on("r-processx@3.8.2:", type=("build", "run"))
	depends_on("r-ps@1.7.5:", type=("build", "run"))
	depends_on("r-r6@2.5.1:", type=("build", "run"))
	depends_on("r-rlang@1.1.1:", type=("build", "run"))
	depends_on("r-waldo@0.5.1:", type=("build", "run"))
	depends_on("r-withr@2.5:", type=("build", "run"))
