# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetaliteTable1(RPackage):
	"""Interactive Table of Descriptive Statistics in HTML

	Create an interactive table of descriptive statistics in HTML. 
  This table is typically used for exploratory analysis in a clinical study (referred to as 'Table 1').
	"""
	
	cran = "metalite.table1" 

	version("0.3.0", md5="b6019f5e5e3477b23c7f6edb1a91c58d", url="https://cran.r-project.org/src/contrib/metalite.table1_0.3.0.tar.gz")

	depends_on("r-metalite", type=("build", "run"))
	depends_on("r-reactable", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-r2rtf", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
