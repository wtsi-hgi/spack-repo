# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastdigest(RPackage):
	"""Fast, Low Memory-Footprint Digests of R Objects.

	Provides an R interface to Bob Jenkin's streaming, non-cryptographic
	'SpookyHash' hash algorithm for use in digest-based comparisons of R
	objects. 'fastdigest' plugs directly into R's internal serialization
	machinery, allowing digests of all R objects the serialize() function
	supports, including reference-style objects via custom hooks. Speed is high
	and scales linearly by object size; memory usage is constant and
	negligible."""

	cran = "fastdigest"

	maintainers("dorton21")

	license("Artistic-2.0")

	version("0.6-3", md5="ed60da6cded36a298ef6215aaae897b0")

