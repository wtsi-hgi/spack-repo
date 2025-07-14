# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPanelcnMops(RPackage):
	"""CNV detection tool for targeted NGS panel data

	CNV detection tool for targeted NGS panel data. Extension of the cn.mops package.
	"""
	
	bioc = "panelcn.mops"

	version("1.30.0", commit="89cf5c47086da0bfc7404ccbc41860e84e3c4d06")
	version("1.24.0", commit="5810f7814366f1fa206a7e13c4449f99f4b54f06")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cn-mops", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
