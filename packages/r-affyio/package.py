# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAffyio(RPackage):
	"""Tools for parsing Affymetrix data files.

	Routines for parsing Affymetrix data files based upon file format
	information. Primary focus is on accessing the CEL and CDF file
	formats."""

	bioc = "affyio"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/affyio_1.72.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/affyio/affyio_1.72.0.tar.gz"]

	version("1.72.0", md5="9bd1e4acedbf756386f96d4c1ebb21f3")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-zlibbioc", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
