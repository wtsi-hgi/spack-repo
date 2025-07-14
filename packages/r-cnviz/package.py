# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCnviz(RPackage):
	"""Copy Number Visualization

	CNViz takes probe, gene, and segment-level log2 copy number ratios and launches a Shiny app to visualize your sample's copy number profile. You can also integrate loss of heterozygosity (LOH) and single nucleotide variant (SNV) data.
	"""
	
	bioc = "CNViz"

	version("1.16.0", commit="f7897dcc9a110766fa7463153216c1de5c7804a6")
	version("1.10.0", commit="eb85b67525b1c3762daca962e0b74330b53d560f")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-shiny@1.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-karyoploter", type=("build", "run"))
	depends_on("r-copynumberplots", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
