# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPeerperformance(RPackage):
	"""Luck-Corrected Peer Performance Analysis in R

	Provides functions to perform the peer performance
    analysis of funds' returns as described in Ardia and Boudt (2018) <doi:10.1016/j.jbankfin.2017.10.014>.
	"""
	
	homepage = "https://github.com/ArdiaD/PeerPerformance"
	cran = "PeerPerformance" 

	version("2.2.5", md5="6fb52fb412d63c2b8ebaf33afbedb47b")

	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
