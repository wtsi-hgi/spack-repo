# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatstatUtils(RPackage):
	"""Utility Functions for 'spatstat'.

	Contains utility functions for the 'spatstat' package which may also be
	useful for other purposes."""

	cran = "spatstat.utils"

	version("3.0-4", md5="70415642c5b389be236e855a4db39925")

	depends_on("r@3.3:", type=("build", "run"))
