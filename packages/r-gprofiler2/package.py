# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGprofiler2(RPackage):
	"""Interface to the 'g:Profiler' Toolset

	A toolset for functional enrichment analysis and visualization, gene/protein/SNP identifier conversion and mapping orthologous genes across species via 'g:Profiler' (<https://biit.cs.ut.ee/gprofiler/>). 
    The main tools are: 
    (1) 'g:GOSt' - functional enrichment analysis and visualization of gene lists; 
    (2) 'g:Convert' - gene/protein/transcript identifier conversion across various namespaces;
    (3) 'g:Orth' - orthology search across species;
    (4) 'g:SNPense' - mapping SNP rs identifiers to chromosome positions, genes and variant effects.
    This package is an R interface corresponding to the 2019 update of 'g:Profiler' and provides access to 'g:Profiler' for versions 'e94_eg41_p11' and higher. See the package 'gProfileR' for accessing older versions from the 'g:Profiler' toolset.  
	"""
	
	cran = "gprofiler2" 

	version("0.2.2", md5="74abfbe7f9fd042230dc18bbfd90fd1f", url="https://cran.r-project.org/src/contrib/gprofiler2_0.2.2.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-crosstalk", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
