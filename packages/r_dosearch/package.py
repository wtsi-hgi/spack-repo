# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDosearch(RPackage):
	"""Causal Effect Identification from Multiple Incomplete Data
Sources

	Identification of causal effects from arbitrary observational and experimental probability distributions via do-calculus and standard probability manipulations using a search-based algorithm by Tikka et al. (2021) <doi:10.18637/jss.v099.i05>. Allows for the presence of mechanisms related to selection bias (Bareinboim, E. and Tian, J. (2015) <http://ftp.cs.ucla.edu/pub/stat_ser/r445.pdf>), transportability (Bareinboim, E. and Pearl, J. (2014) <http://ftp.cs.ucla.edu/pub/stat_ser/r443.pdf>), missing data (Mohan, K. and Pearl, J. and Tian., J. (2013) <http://ftp.cs.ucla.edu/pub/stat_ser/r410.pdf>) and arbitrary combinations of these. Also supports identification in the presence of context-specific independence (CSI) relations through labeled directed acyclic graphs (LDAG). For details on CSIs see Corander et al. (2019) <doi:10.1016/j.apal.2019.04.004>. 
	"""
	
	cran = "dosearch" 

	version("1.0.8", md5="1a5f2a1d946cc6bf725b7028c6a282af")

	depends_on("r-rcpp", type=("build", "run"))
