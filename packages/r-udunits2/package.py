# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUdunits2(RPackage):
	"""Udunits-2 Bindings for R.

	Provides simple bindings to Unidata's udunits library."""

	cran = "udunits2"

	version("0.13.2.1", md5="33253bd0b48ade3601fa220cf193de93", url="https://cran.r-project.org/src/contrib/udunits2_0.13.2.1.tar.gz")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("udunits@2:", type=("build", "link", "run"))
