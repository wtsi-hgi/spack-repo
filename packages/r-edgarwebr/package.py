# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REdgarwebr(RPackage):
	"""SEC Filings Access

	A set of methods to access and parse live filing information from the
    U.S. Securities and Exchange Commission (SEC - <https://www.sec.gov/>) including
    company and fund filings along with all associated metadata.
	"""
	
	homepage = "https://mwaldstein.github.io/edgarWebR/"
	cran = "edgarWebR" 

	version("1.1.0", md5="c44775fa75335432b8863793428d95ee")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-xml2@1.3.2:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
