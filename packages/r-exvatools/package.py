# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExvatools(RPackage):
	"""Value Added in Exports and Other Input-Output Table Analysis
Tools

	Analysis of trade in value added with international
    input-output tables. Includes commands for easy data extraction,
    matrix manipulation, decomposition of value added in gross exports and
    calculation of value added indicators, with full geographical and
    sector customization.  Decomposition methods include Borin and Mancini
    (2023) <doi:10.1080/09535314.2022.2153221>, Miroudot and Ye (2021)
    <doi:10.1080/09535314.2020.1730308>, Wang et al. (2013)
    <https://econpapers.repec.org/paper/nbrnberwo/19677.htm> and Koopman
    et al. (2014) <doi:10.1257/aer.104.2.459>.
	"""
	
	cran = "exvatools" 

	version("0.6.0", md5="c34a2b097408d2a58dd7e17980435622")
	version("0.7.0", md5="b13b60f8b09ed11853f85bec66f3c149")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
