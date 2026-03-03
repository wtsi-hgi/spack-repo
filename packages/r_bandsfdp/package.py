# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBandsfdp(RPackage):
	"""Compute Upper Prediction Bounds on the FDP in Competition-Based
Setups

	Implements functions that calculate upper prediction 
  bounds on the false discovery proportion (FDP) in the list of discoveries 
  returned by competition-based setups, implementing Ebadi et al. (2022)
  <arXiv:2302.11837>. Such setups include target-decoy competition (TDC) 
  in computational mass spectrometry and the knockoff construction in linear 
  regression (note this package typically uses the terminology of TDC). Included 
  is the standardized (TDC-SB) and uniform (TDC-UB) bound on TDC's FDP, and the 
  simultaneous standardized and uniform bands. Requires 
  pre-computed Monte Carlo statistics available at 
  <https://github.com/uni-Arya/fdpbandsdata>. This data can be downloaded by
  running the command 'devtools::install_github("uni-Arya/fdpbandsdata")' in R
  and restarting R after installation. The size of this data is roughly 81Mb.
	"""
	
	homepage = "https://github.com/uni-Arya/bandsfdp"
	cran = "bandsfdp" 

	version("1.1.0", md5="0d12eb774310c1abce9b13228873accd")

