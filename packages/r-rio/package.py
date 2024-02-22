# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRio(RPackage):
	"""A Swiss-Army Knife for Data I/O.

	Streamlined data import and export by making assumptions that the user
	is probably willing to make: 'import()' and 'export()' determine the data
	structure from the file extension, reasonable defaults are used for data
	import and export (e.g., 'stringsAsFactors=FALSE'), web-based import is
	natively supported (including from SSL/HTTPS), compressed files can be read
	directly without explicit decompression, and fast import packages are used
	where appropriate. An additional convenience function, 'convert()',
	provides a simple method for converting between file types."""

	cran = "rio"

	version("1.0.1", md5="10999152910a11bcccc2b85e78cfda4f")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-haven@1.1.2:", type=("build", "run"))
	depends_on("r-curl@0.6:", type=("build", "run"))
	depends_on("r-data-table@1.11.2:", type=("build", "run"))
	depends_on("r-readxl@0.1.1:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-writexl", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
