# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChampdata(RPackage):
	"""Packages for ChAMP package.

	Provides datasets needed for ChAMP including a test dataset and blood
	controls for CNA analysis."""

	bioc = "ChAMPdata"
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/ChAMPdata_2.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/ChAMPdata/ChAMPdata_2.34.0.tar.gz"]

	version("2.34.0", md5="b12bfec01a1cfdd103bc0cb9bd44d4aa")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges@1.22.4:", type=("build", "run"))
	depends_on("r-biocgenerics@0.16.1:", type=("build", "run"))

	# experiment