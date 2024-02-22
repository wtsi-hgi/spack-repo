# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPmparser(RPackage):
	"""Create and Maintain a Relational Database of Data from
PubMed/MEDLINE

	Provides a simple interface for extracting various elements from
  the publicly available PubMed XML files, incorporating PubMed's regular
  updates, and combining the data with the NIH Open Citation Collection. See
  Schoenbachler and Hughey (2021) <doi:10.7717/peerj.11071>.
	"""
	
	homepage = "https://pmparser.hugheylab.org"
	cran = "pmparser" 

	version("1.0.20", md5="cdfb65f054da179c795c8c89f9075872")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-curl@4.3.2:", type=("build", "run"))
	depends_on("r-data-table@1.12.2:", type=("build", "run"))
	depends_on("r-dbi@1.1:", type=("build", "run"))
	depends_on("r-foreach@1.5:", type=("build", "run"))
	depends_on("r-glue@1.4.2:", type=("build", "run"))
	depends_on("r-iterators@1.0.12:", type=("build", "run"))
	depends_on("r-jsonlite@1.7:", type=("build", "run"))
	depends_on("r-r-utils@2.10.1:", type=("build", "run"))
	depends_on("r-rcurl@1.98:", type=("build", "run"))
	depends_on("r-withr@2.3:", type=("build", "run"))
	depends_on("r-xml2@1.3.3:", type=("build", "run"))
	depends_on("unzip", type=("build", "link", "run"))
	depends_on("sqlite", type=("build", "link", "run"))
