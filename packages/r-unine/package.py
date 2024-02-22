# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUnine(RPackage):
	"""Unine Light Stemmer

	Implementation of "light" stemmers for French, German, Italian, Spanish, Portuguese, Finnish, Swedish. 
  They are based on the same work as the "light" stemmers found in 'SolR' <https://lucene.apache.org/solr/> or 'ElasticSearch' <https://www.elastic.co/fr/products/elasticsearch>. 
  A "light" stemmer consists in removing inflections only for noun and adjectives. 
  Indexing verbs for these languages is not of primary importance compared to nouns and adjectives. 
  The stemming procedure for French is described in (Savoy, 1999) <doi:10.1002/(SICI)1097-4571(1999)50:10%3C944::AID-ASI9%3E3.3.CO;2-H>.
	"""
	
	homepage = "https://github.com/pommedeterresautee/unine"
	cran = "unine" 

	version("0.2.0", md5="707f99cc2d10949285bed2e95f0a3446")

	depends_on("r-rcpp", type=("build", "run"))
