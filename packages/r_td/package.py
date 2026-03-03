# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTd(RPackage):
	"""Access to the 'twelvedata' Financial Data API

	The 'twelvedata' REST service offers access to current and historical
 data on stocks, standard as well as digital 'crypto' currencies, and other financial
 assets covering a wide variety of course and time spans. See <https://twelvedata.com/>
 for details, to create an account, and to request an API key for free-but-capped access
 to the data.
	"""
	
	homepage = "https://dirk.eddelbuettel.com/code/td.html"
	cran = "td" 

	version("0.0.6", md5="9bcaf1fcffa02d04764d73d9cd60fc6d")

	depends_on("r-rcppsimdjson", type=("build", "run"))
