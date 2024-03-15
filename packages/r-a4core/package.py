# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RA4core(RPackage):
	"""Automated Affymetrix Array Analysis Core Package.

	Utility functions for the Automated Affymetrix Array Analysis set of
	packages."""

	bioc = "a4Core"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/a4Core_1.50.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/a4Core/a4Core_1.50.0.tar.gz"]

	version("1.50.0", md5="fdca418afe3a74d9114d8d28afca2037")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
