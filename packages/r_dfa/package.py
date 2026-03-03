# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDfa(RPackage):
	"""Detrended Fluctuation Analysis

	Containing the Detrended Fluctuation Analysis (DFA), Detrended Cross-Correlation Analysis (DCCA), Detrended Cross-Correlation Coefficient (rhoDCCA), Delta Amplitude Detrended Cross-Correlation Coefficient (DeltarhoDCCA), log amplitude Detrended Fluctuation Analysis (DeltalogDFA), and the Activity Balance Index, it also includes two DFA automatic methods for identifying crossover points and a Deltalog automatic method for identifying reference channels.
	"""
	
	cran = "DFA" 

	version("1.0.0", md5="a74cc0c077b257cde8db326a66e5ffa5")

	depends_on("r@3.5:", type=("build", "run"))
