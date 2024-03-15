# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIso(RPackage):
	"""Functions to Perform Isotonic Regression.

	Linear order and unimodal order (univariate) isotonic regression; bivariate
	isotonic regression with linear order on both variables."""

	cran = "Iso"

	version("0.0-21", md5="4f9172d1c292a3a7fd9a40c034197e94")

	depends_on("r@1.7:", type=("build", "run"))
