# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRelevance(RPackage):
	"""Calculate Relevance and Significance Measures

	Calculates relevance and significance values for
  simple models and for many types of regression models.
  These are introduced in
  'Stahel, Werner A.' (2021)
  "Measuring Significance and Relevance instead of p-values."
  <https://stat.ethz.ch/~stahel/relevance/stahel-relevance2103.pdf>.
  These notions are also applied to replication studies,
  as described in the manuscript
  'Stahel, Werner A.' (2022)
  "'Replicability': Terminology, Measuring Success, and Strategy"
  available in the documentation.
	"""
	
	cran = "relevance" 

	version("2.1", md5="1fa21ba95a8f665b498a626a6455f3c5")

	depends_on("r@3.5:", type=("build", "run"))
