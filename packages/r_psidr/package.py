# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsidr(RPackage):
	"""Build Panel Data Sets from PSID Raw Data

	Makes it easy to build panel data in wide format from Panel Survey
    of Income Dynamics ('PSID') delivered raw data. Downloads data directly from
    the PSID server using the 'SAScii' package. 'psidR' takes care of merging
    data from each wave onto a cross-period index file, so that individuals can be
    followed over time. The user must specify which years they are interested in,
    and the 'PSID' variable names (e.g. ER21003) for each year (they differ in each
    year). The package offers helper functions to retrieve variable names from different
    waves. There are different panel data designs and sample subsetting criteria
    implemented ("SRC", "SEO", "immigrant" and "latino" samples).
	"""
	
	homepage = "https://github.com/floswald/psidR"
	cran = "psidR" 

	version("2.1", md5="8b7c338825051b1c29610289266de569")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-sascii", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-futile-logger", type=("build", "run"))
