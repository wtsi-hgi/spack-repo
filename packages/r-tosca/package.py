# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTosca(RPackage):
	"""Tools for Statistical Content Analysis

	A framework for statistical analysis in content analysis. In addition to a pipeline for preprocessing text corpora and linking to the latent Dirichlet allocation from the 'lda' package, plots are offered for the descriptive analysis of text corpora and topic models. In addition, an implementation of Chang's intruder words and intruder topics is provided. Sample data for the vignette is included in the toscaData package, which is available on gitHub: <https://github.com/Docma-TU/toscaData>.
	"""
	
	homepage = "https://github.com/Docma-TU/tosca"
	cran = "tosca" 

	version("0.3-2", md5="b2df4785cd745da2c059b7893a412665")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tm@0.7.5:", type=("build", "run"))
	depends_on("r-lda@1.4.2:", type=("build", "run"))
	depends_on("r-quanteda@1.4:", type=("build", "run"))
	depends_on("r-lubridate@1.7.3:", type=("build", "run"))
	depends_on("r-htmltools@0.3.6:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.2:", type=("build", "run"))
	depends_on("r-stringr@1.3.1:", type=("build", "run"))
	depends_on("r-wikipedir@1.5:", type=("build", "run"))
	depends_on("r-data-table@1.11.4:", type=("build", "run"))
