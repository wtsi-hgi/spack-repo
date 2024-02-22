# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeneplotter(RPackage):
	"""Graphics related functions for Bioconductor.

	Functions for plotting genomic data."""

	bioc = "geneplotter"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/geneplotter_1.80.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/geneplotter/geneplotter_1.80.0.tar.gz"]

	version("1.80.0", md5="29d4ec34db2e953fc9b7306f4d3b7733")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-annotate", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
