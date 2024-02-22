# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTratamentosAd(RPackage):
	"""Pacote Para Analise De Experimentos Com Testemunhas Adicionais

	Pacote para a analise de experimentos com um ou dois fatores com
             testemunhas adicionais conduzidos no delineamento inteiramente 
             casualizado ou em blocos casualizados. 
             "Package for the analysis of one or two-way experiments with 
             additional controls conducted in a completely randomized design 
             or in a randomized block design".
	"""
	
	cran = "Tratamentos.ad" 

	version("0.2.4", md5="c28a0db4b4ee206417f5aa86b8f4cc5b")

	depends_on("r-crayon", type=("build", "run"))
