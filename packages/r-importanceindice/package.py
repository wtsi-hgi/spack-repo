# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImportanceindice(RPackage):
	"""Analyzing Data Through of Percentage of Importance Indice and
Its Derivations

	The Percentage of Importance Indice (Percentage_I.I.) bases in magnitudes, frequencies, and distributions of occurrence of an event (DEMOLIN-LEITE, 2021) <http://cjascience.com/index.php/CJAS/article/view/1009/1350>. This index can detect the key loss sources (L.S) and solution sources (S.S.), classifying them according to their importance in terms of loss or income gain, on the productive system. The Percentage_I.I. = [(ks1 x c1 x ds1)/SUM (ks1 x c1 x ds1) + (ks2 x c2 x ds2) + (ksn x cn x dsn)] x 100. key source (ks) is obtained using simple regression analysis and magnitude (abundance). Constancy (c) is SUM of occurrence of L.S. or S.S. on the samples (absence = 0 or presence = 1), and distribution source (ds) is obtained using chi-square test. This index has derivations: i.e., i) Loss estimates and solutions effectiveness and ii) Attention and non-attention levels (DEMOLIN-LEITE,2024) <DOI: 10.1590/1519-6984.253215>.
	"""
	
	cran = "ImportanceIndice" 

	version("0.0.2", md5="03b4cda5acbd99e8668006ba2380ad0f")

	depends_on("r-crayon", type=("build", "run"))
