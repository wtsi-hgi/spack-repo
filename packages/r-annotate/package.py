# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnnotate(RPackage):
	"""Annotation for microarrays.

	Using R enviroments for annotation."""

	bioc = "annotate"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/annotate_1.80.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/annotate/annotate_1.80.0.tar.gz"]

	version("1.80.0", md5="04d25cadc03401556364f8ca9c3b2a61")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-annotationdbi@1.27.5:", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-biocgenerics@0.13.8:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
