# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPatchwork(RPackage):
	"""The Composer of Plots.

	The 'ggplot2' package provides a strong API for sequentially building up a
	plot, but does not concern itself with composition of multiple plots.
	'patchwork' is a package that expands the API to allow for arbitrarily
	complex composition of plots by, among others, providing mathematical
	operators for combining multiple plots. Other packages that try to address
	this need (but with a different approach) are 'gridExtra' and 'cowplot'."""

	license("MIT")

	cran = "patchwork"
	version("1.3.2", sha256="0ec469acfd69d1a4f1a6317c861e6bf000f768c2d5047e3aed6713df9afe27eb")
	version("1.3.1", sha256="e3e7ba0052b12649eb04c1f10317bef626167a4de37b26f662933490434591be")
	version("1.3.0", sha256="77af6ec4a4aacebd9b5ba128d97d2fb10cfc4e4c40aded942d6976bab3e52e16")
	version("1.2.0", sha256="cc31ea13560c424de9bfe2287d926a7d9e6cc8da2d5561402bb145b4f51b68a1")
	version("1.1.3", sha256="e976424f4bd88e075f2ca6836db2aa1eb5fa7ad6a20ad0a34a4d5047d59ad71e")
	version("1.1.2", sha256="dab9d5d2d704d591717eaa6efeacf09cb6cd7bee2ca2c46d18414e8503ac8977")
	version("1.1.1", sha256="cf0d7d9f92945729b499d6e343441c55007d5b371206d5389b9e5154dc7cf481")
	version("1.1.0", sha256="93f97064a3300d35ba155dd247d45fbfa06e72c30d037ecf97b5a9ead8e67a8f")
	version("1.0.1", sha256="02bcc43ca778a0f981fd7f36c0b15b0d1eb8ed87d3db0b8bfd33b708881aa972")
	version("1.0.0", sha256="8bfb59b91775781848f39eedcaaaf92c147e2637f384085fcdd41fc8355b3c63")

	depends_on("r-ggplot2@3.0.0:", type=("build", "run"))

	depends_on("r-gtable@0.3.6:", type=("build", "run"), when="@1.3.0:")
	depends_on("r-gtable@:0.3.6", type=("build", "run"), when="@:1.2.0")

	depends_on("r-rlang@1.0.0:", type=("build", "run"), when="@1.3.0:")
	depends_on("r-rlang", type=("build", "run"), when="@:1.3.0")

	depends_on("r-cli", type=("build", "run"), when="@1.1.3:")

	depends_on("r-farver", type=("build", "run"), when="@1.3.0:")

	def patch(self):
		if self.spec.satisfies("@1.3.2:"):
			filter_file(
				"  run_on_load()",
				"""  run_on_load()
  ns <- asNamespace("ggplot2")
  if (exists("is_ggplot", envir = ns, inherits = FALSE)) {
    is_ggplot <<- get("is_ggplot", envir = ns)
  } else if (exists("is.ggplot", envir = ns, inherits = FALSE)) {
    is_ggplot <<- get("is.ggplot", envir = ns)
  }
  if (exists("is_theme", envir = ns, inherits = FALSE)) {
    is_theme <<- get("is_theme", envir = ns)
  } else if (exists("is.theme", envir = ns, inherits = FALSE)) {
    is_theme <<- get("is.theme", envir = ns)
  }
""",
				"R/zzz.R",
				string=True,
			)
			filter_file(
				"importFrom(ggplot2,is_ggplot)\n",
				"",
				"NAMESPACE",
				string=True,
			)
			filter_file(
				"importFrom(ggplot2,is_theme)\n",
				"",
				"NAMESPACE",
				string=True,
			)
			force_remove("MD5")
