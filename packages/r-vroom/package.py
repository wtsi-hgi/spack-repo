# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVroom(RPackage):
	"""Read and Write Rectangular Text Data Quickly.

	The goal of 'vroom' is to read and write data (like 'csv', 'tsv' and
	'fwf') quickly. When reading it uses a quick initial indexing step, then
	reads the values lazily , so only the data you actually use needs to be
	read. The writer formats the data in parallel and writes to disk
	asynchronously from formatting."""

	cran = "vroom"

	license("MIT")

	version("1.6.5", md5="8e6351782f34b6ae20bdc66836b52052")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-bit64", type=("build", "run"))
	depends_on("r-cli@3.2:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-hms", type=("build", "run"))
	depends_on("r-lifecycle@1.0.3:", type=("build", "run"))
	depends_on("r-rlang@0.4.2:", type=("build", "run"))
	depends_on("r-tibble@2:", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-tzdb@0.1.1:", type=("build", "run"))
	depends_on("r-vctrs@0.2:", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-cpp11@0.2:", type=("build", "run"))
	depends_on("r-progress@1.2.1:", type=("build", "run"))
