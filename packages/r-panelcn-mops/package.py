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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/panelcn.mops_1.24.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/panelcn.mops/panelcn.mops_1.24.0.tar.gz"]

	version("1.24.0", md5="c40de00a870c4b693e6312b7d2110b96")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cn-mops", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
