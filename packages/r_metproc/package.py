# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetproc(RPackage):
	"""Separate Metabolites into Likely Measurement Artifacts and True
Metabolites

	Split an untargeted metabolomics data set into a set of likely true 
    metabolites and a set of likely measurement artifacts. This process involves 
    comparing missing rates of pooled plasma samples and biological samples. The 
    functions assume a fixed injection order of samples where biological samples are 
    randomized and processed between intermittent pooled plasma samples. By comparing 
    patterns of missing data across injection order, metabolites that appear in blocks
    and are likely artifacts can be separated from metabolites that seem to have 
    random dispersion of missing data. The two main metrics used are: 1. the number of 
    consecutive blocks of samples with present data and 2. the correlation of missing rates 
    between biological samples and flanking pooled plasma samples.
	"""
	
	cran = "MetProc" 

	version("1.0.1", md5="0eff882c18db074e00c0609514301526")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-fastcluster", type=("build", "run"))
