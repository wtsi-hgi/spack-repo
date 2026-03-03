# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConfreq(RPackage):
	"""Configural Frequencies Analysis Using Log-Linear Modeling

	Offers several functions for Configural Frequencies
    Analysis (CFA), which is a useful statistical tool for the analysis of
    multiway contingency tables. CFA was introduced by G. A. Lienert as
    'Konfigurations Frequenz Analyse - KFA'. Lienert, G. A. (1971). 
    Die Konfigurationsfrequenzanalyse: I. Ein neuer Weg zu Typen und Syndromen. 
    Zeitschrift für Klinische Psychologie und Psychotherapie, 19(2), 99–115.
	"""
	
	cran = "confreq" 

	version("1.6.1-1", md5="c96b9ed073572e2f6d0d2c77f78fb23e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gmp", type=("build", "run"))
	depends_on("r-vcd", type=("build", "run"))
