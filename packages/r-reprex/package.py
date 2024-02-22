# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReprex(RPackage):
	"""Prepare Reproducible Example Code via the Clipboard.

	Convenience wrapper that uses the 'rmarkdown' package to render small
	snippets of code to target formats that include both code and output.  The
	goal is to encourage the sharing of small, reproducible, and runnable
	examples on code-oriented websites, such as <https://stackoverflow.com/>
	and <https://github.com>, or in email.  'reprex' also extracts clean,
	runnable R code from various common formats, such as copy/paste from an R
	session."""

	cran = "reprex"

	version("2.1.0", md5="f9c998d2dc355b00fbde58c04d97d220")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-callr@3.6:", type=("build", "run"))
	depends_on("r-cli@3.2:", type=("build", "run"))
	depends_on("r-clipr@0.4:", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-knitr@1.23:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-withr@2.3:", type=("build", "run"))
	depends_on("pandoc@2.0:", type=("build", "link", "run"))
