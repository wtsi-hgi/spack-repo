# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParallelly(RPackage):
	"""Enhancing the 'parallel' Package.

	Utility functions that enhance the 'parallel' package and support the
	built-in parallel backends of the 'future' package. For example,
	availableCores() gives the number of CPU cores available to your R process
	as given by the operating system, 'cgroups' and Linux containers, R
	options, and environment variables, including those set by job schedulers
	on high-performance compute clusters. If none is set, it will fall back to
	parallel::detectCores(). Another example is makeClusterPSOCK(), which is
	backward compatible with parallel::makePSOCKcluster() while doing a better
	job in setting up remote cluster workers without the need for configuring
	the firewall to do port-forwarding to your local computer."""

	cran = "parallelly"

	license("LGPL-2.1-or-later")

	version("1.37.1", md5="d9f4f8ef7f775f0b3c40ee606a482917")

