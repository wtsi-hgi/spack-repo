# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RA4preproc(RPackage):
	"""Automated Affymetrix Array Analysis Preprocessing Package.

	Utility functions to pre-process data for the Automated Affymetrix Array
	Analysis set of packages."""

	bioc = "a4Preproc"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/a4Preproc_1.50.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/a4Preproc/a4Preproc_1.50.0.tar.gz"]

	version("1.50.0", md5="5d9eea3d9957fc99156115052398f0cb")

	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
