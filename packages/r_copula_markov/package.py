# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCopulaMarkov(RPackage):
	"""Copula-Based Estimation and Statistical Process Control for
Serially Correlated Time Series

	Estimation and statistical process control are performed under
 copula-based time-series models.
 Available are statistical methods in Long and Emura (2014 JCSA),
 Emura et al. (2017 Commun Stat-Simul) <DOI:10.1080/03610918.2015.1073303>,
 Huang and Emura (2021 Commun Stat-Simul) <DOI:10.1080/03610918.2019.1602647>,
 Lin et al. (2021 Comm Stat-Simul) <DOI:10.1080/03610918.2019.1652318>,
 Sun et al. (2020 JSS Series in Statistics)<DOI:10.1007/978-981-15-4998-4>,
 and Huang and Emura (2021, in revision).
	"""
	
	cran = "Copula.Markov" 

	version("2.9", md5="a1887269f423da56d690f55952bc2b2a")

