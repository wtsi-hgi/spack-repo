# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFutureApply(RPackage):
	"""Apply Function to Elements in Parallel using Futures.

	Implementations of apply(), by(), eapply(), lapply(), Map(), mapply(),
	replicate(), sapply(), tapply(), and vapply() that can be resolved using
	any future-supported backend, e.g. parallel on the local machine or
	distributed on a compute cluster. These future_*apply() functions come with
	the same pros and cons as the corresponding base-R *apply() functions but
	with the additional feature of being able to be processed via the future
	framework."""

	cran = "future.apply"

	version("1.11.1", md5="44e4c075314f465342c54a3b15e066d1")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-future@1.28:", type=("build", "run"))
	depends_on("r-globals@0.16.1:", type=("build", "run"))
