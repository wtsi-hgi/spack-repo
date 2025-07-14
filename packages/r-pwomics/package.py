# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPwomics(RPackage):
	"""Pathway-based data integration of omics data

	pwOmics performs pathway-based level-specific data comparison of matching omics data sets based on pre-analysed user-specified lists of differential genes/transcripts and phosphoproteins. A separate downstream analysis of phosphoproteomic data including pathway identification, transcription factor identification and target gene identification is opposed to the upstream analysis starting with gene or transcript information as basis for identification of upstream transcription factors and potential proteomic regulators. The cross-platform comparative analysis allows for comprehensive analysis of single time point experiments and time-series experiments by providing static and dynamic analysis tools for data integration. In addition, it provides functions to identify individual signaling axes based on data integration.
	"""
	
	bioc = "pwOmics"

	version("1.34.0", commit="dc5bce7e4ff4945436467843ac323bf2c0d67185")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rbiopaxparser", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-stringdb", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
