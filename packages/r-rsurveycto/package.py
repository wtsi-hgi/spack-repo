# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsurveycto(RPackage):
	"""Interact with Data on 'SurveyCTO'

	'SurveyCTO' is a platform for mobile data collection in offline settings.
  The 'rsurveycto' R package uses the 'SurveyCTO' REST API
  <https://docs.surveycto.com/05-exporting-and-publishing-data/05-api-access/01.api-access.html>
  to read datasets and forms from a 'SurveyCTO' server into R as 'data.table's
  and to download file attachments. The package also has limited support to
  write datasets to a server.
	"""
	
	homepage = "https://agency-fund.github.io/rsurveycto/"
	cran = "rsurveycto" 

	version("0.1.6", md5="1e457f8cd6ad8bdce72392f4c86c3c4c")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-checkmate@2.1:", type=("build", "run"))
	depends_on("r-cli@3.4:", type=("build", "run"))
	depends_on("r-curl@4.3.2:", type=("build", "run"))
	depends_on("r-data-table@1.14.8:", type=("build", "run"))
	depends_on("r-glue@1.6.2:", type=("build", "run"))
	depends_on("r-httr@1.4.3:", type=("build", "run"))
	depends_on("r-jsonlite@1.8:", type=("build", "run"))
	depends_on("r-rlang@1.0.5:", type=("build", "run"))
	depends_on("r-withr@2.5:", type=("build", "run"))
