# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvarPt(RPackage):
	"""Analise multivariada (brazilian portuguese)

	Pacote para analise multivariada, tendo funcoes que executam analise de correspondencia simples (CA) e multipla (MCA), analise de componentes principais (PCA), analise de correlacao canonica (CCA), analise fatorial (FA), escalonamento multidimensional (MDS), analise discriminante linear (LDA) e quadratica (QDA), analise de cluster hierarquico e nao hierarquico, regressao linear simples e multipla, analise de multiplos fatores (MFA) para dados quantitativos, qualitativos, de frequencia (MFACT) e dados mistos, biplot, scatter plot, projection pursuit (PP), grant tour e outras funcoes uteis para a analise multivariada.
	"""
	
	cran = "MVar.pt" 

	version("2.2.1", md5="212a8c7f81f6947036078cc1c5a811ce")

	depends_on("r-mass", type=("build", "run"))
