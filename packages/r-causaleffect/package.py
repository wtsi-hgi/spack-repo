# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCausaleffect(RPackage):
	"""Deriving Expressions of Joint Interventional Distributions and
Transport Formulas in Causal Models

	Functions for identification and transportation of causal effects. Provides a conditional causal effect identification algorithm (IDC) by Shpitser, I. and Pearl, J. (2006) <http://ftp.cs.ucla.edu/pub/stat_ser/r329-uai.pdf>, an algorithm for transportability from multiple domains with limited experiments by Bareinboim, E. and Pearl, J. (2014) <http://ftp.cs.ucla.edu/pub/stat_ser/r443.pdf>, and a selection bias recovery algorithm by Bareinboim, E. and Tian, J. (2015) <http://ftp.cs.ucla.edu/pub/stat_ser/r445.pdf>. All of the previously mentioned algorithms are based on a causal effect identification algorithm by Tian , J. (2002) <http://ftp.cs.ucla.edu/pub/stat_ser/r309.pdf>.
	"""
	
	homepage = "https://github.com/santikka/causaleffect/"
	cran = "causaleffect" 

	version("1.3.15", md5="48abded5e991063e7a6d2df5f72367ca")

	depends_on("r-igraph", type=("build", "run"))
