# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAffydata(RPackage):
	"""Affymetrix Data for Demonstration Purpose.

	Example datasets of a slightly large size. They represent 'real world
	examples', unlike the artificial examples included in the package
	affy."""

	bioc = "affydata"
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/affydata_1.50.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/affydata/affydata_1.50.0.tar.gz"]

	version("1.50.0", md5="29caf389ca94d4c0c0b27d993f33354c")

	depends_on("r@2.4:", type=("build", "run"))
	depends_on("r-affy@1.23.4:", type=("build", "run"))

	# experiment