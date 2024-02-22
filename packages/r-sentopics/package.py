# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSentopics(RPackage):
	"""Tools for Joint Sentiment and Topic Analysis of Textual Data

	A framework that joins topic modeling and sentiment analysis of
  textual data. The package implements a fast Gibbs sampling estimation of
  Latent Dirichlet Allocation (Griffiths and Steyvers (2004)
  <doi:10.1073/pnas.0307752101>) and Joint Sentiment/Topic Model (Lin, He,
  Everson and Ruger (2012) <doi:10.1109/TKDE.2011.48>). It offers a variety of
  helpers and visualizations to analyze the result of topic modeling. The
  framework also allows enriching topic models with dates and externally
  computed sentiment measures. A flexible aggregation scheme enables the
  creation of time series of sentiment or topical proportions from the enriched
  topic models. Moreover, a novel method jointly aggregates topic proportions
  and sentiment measures to derive time series of topical sentiment.
	"""
	
	homepage = "https://github.com/odelmarcelle/sentopics"
	cran = "sentopics" 

	version("0.7.2", md5="ed9ae05ce7083e70ed8667ad79bbc823")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-quanteda@3.2:", type=("build", "run"))
	depends_on("r-data-table@1.13.6:", type=("build", "run"))
	depends_on("r-rcpphungarian", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
