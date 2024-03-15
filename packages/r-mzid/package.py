# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMzid(RPackage):
	"""An mzIdentML parser for R.

	A parser for mzIdentML files implemented using the XML package. The
	parser tries to be general and able to handle all types of mzIdentML
	files with the drawback of having less 'pretty' output than a vendor
	specific parser. Please contact the maintainer with any problems and
	supply an mzIdentML file so the problems can be fixed quickly."""

	bioc = "mzID"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/mzID_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/mzID/mzID_1.40.0.tar.gz"]

	version("1.40.0", md5="8ede9a6260d4b9aa70edd19838e3c80c")

	depends_on("r-xml", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-protgenerics", type=("build", "run"))
