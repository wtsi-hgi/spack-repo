# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFaulttree(RPackage):
	"""Fault Trees for Risk and Reliability Analysis

	Construction, calculation and display of fault trees. Methods derived from Clifton A. Ericson II (2005, ISBN: 9780471739425) <DOI:10.1002/0471739421>, Antoine Rauzy (1993) <DOI:10.1016/0951-8320(93)90060-C>, Tim Bedford and Roger Cooke (2012, ISBN: 9780511813597) <DOI:10.1017/CBO9780511813597>, Nikolaos Limnios,  (2007, ISBN: 9780470612484) <DOI: 10.1002/9780470612484>.
	"""
	
	homepage = "http://www.openreliability.org/fault-tree-analysis-on-r/"
	cran = "FaultTree" 

	version("1.0.1", md5="aa2d52d86080164275960dc1c4aea960")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
