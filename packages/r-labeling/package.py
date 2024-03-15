# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLabeling(RPackage):
	"""Axis Labeling.

	Provides a range of axis labeling algorithms."""

	cran = "labeling"

	license("MIT OR custom")

	version("0.4.3", md5="915e6c823c1d8243641ce97253389f14")

