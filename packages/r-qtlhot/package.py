# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQtlhot(RPackage):
	"""Inference for QTL Hotspots

	Functions to infer co-mapping trait hotspots and causal models.
  Chaibub Neto E, Keller MP, Broman AF, Attie AD, Jansen RC, Broman KW, Yandell BS (2012) 
  Quantile-based permutation thresholds for QTL hotspots. Genetics 191 : 1355-1365. 
  <doi:10.1534/genetics.112.139451>.
  Chaibub Neto E, Broman AT, Keller MP, Attie AD, Zhang B, Zhu J, Yandell BS (2013)
  Modeling causality for pairs of phenotypes in system genetics. Genetics 193 : 1003-1013.
  <doi:10.1534/genetics.112.147124>.
	"""
	
	homepage = "http://www.stat.wisc.edu/~yandell/statgen"
	cran = "qtlhot" 

	version("1.0.4", md5="3c7c2fa5785e60312150e0142ca1f8fe")

	depends_on("r-qtl", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
