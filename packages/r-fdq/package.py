# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFdq(RPackage):
	"""Forest Data Quality

	
    Forest data quality is a package containing nine methods of analysis for forest databases,
    from databases containing inventory data and growth models, the focus of the analyzes is related to the
    quality of the data present in the database with a focus on consistency , punctuality and completeness of data.
	"""
	
	cran = "fdq" 

	version("0.12", md5="e82d6cf024b35a125cb8da0f58089cd5")

	depends_on("r-fgmutils@0.8:", type=("build", "run"))
	depends_on("r@3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-sqldf", type=("build", "run"))
	depends_on("r-randomcolor", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
