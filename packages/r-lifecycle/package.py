# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLifecycle(RPackage):
	"""Manage the Life Cycle of your Package Functions.

	Manage the life cycle of your exported functions with shared conventions,
	documentation badges, and non-invasive deprecation warnings. The
	'lifecycle' package defines four development stages (experimental,
	maturing, stable, and questioning) and three deprecation stages
	(soft-deprecated, deprecated, and defunct). It makes it easy to insert
	badges corresponding to these stages in your documentation. Usage of
	deprecated functions are signalled with increasing levels of non-invasive
	verbosity."""

	cran = "lifecycle"

	license("MIT")

	version("1.0.4", md5="4490cb8f9777f1ff4bae184d51d24405")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cli@3.4:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
