# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCfid(RPackage):
	"""Identification of Counterfactual Queries in Causal Models

	Facilitates the identification of counterfactual queries in
 structural causal models via the ID* and IDC* algorithms
 by Shpitser, I. and Pearl, J. (2007, 2008) <arXiv:1206.5294>, 
 <https://jmlr.org/papers/v9/shpitser08a.html>. 
 Provides a simple interface for defining causal diagrams and counterfactual 
 conjunctions. Construction of parallel worlds graphs and counterfactual graphs 
 is carried out automatically based on the counterfactual query and the causal 
 diagram. See Tikka, S. (2023) <doi:10.32614/RJ-2023-053> for a tutorial of 
 the package.
	"""
	
	homepage = "https://github.com/santikka/cfid"
	cran = "cfid" 

	version("0.1.7", md5="ee60ae5edfb47b97d3246855b27da3ac")

