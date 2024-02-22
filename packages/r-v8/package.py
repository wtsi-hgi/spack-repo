# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RV8(RPackage):
	"""Embedded JavaScript and WebAssembly Engine for R.

	An R interface to V8: Google's open source JavaScript and WebAssembly
	engine. This package can be compiled either with V8 version 6 and up or
	NodeJS when built as a shared library."""

	cran = "V8"

	version("4.4.2", md5="f34175ae36832619da40067f3d278c46", url="https://cran.r-project.org/src/contrib/V8_4.4.2.tar.gz")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-jsonlite@1:", type=("build", "run"))
	depends_on("r-curl@1:", type=("build", "run"))

	conflicts("@3.4.0", when="target=aarch64:")
	conflicts("@3.4.0", when="%gcc@5:")

	def setup_build_environment(self, env):
		spec = self.spec
		if (spec.platform == "darwin") or (
			spec.platform == "linux" and spec.target.family == "x86_64"
		):
			env.append_flags("DOWNLOAD_STATIC_LIBV8", "1")
