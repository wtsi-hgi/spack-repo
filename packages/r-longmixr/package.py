# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLongmixr(RPackage):
	"""Longitudinal Consensus Clustering with 'flexmix'

	An adaption of the consensus clustering approach from
    'ConsensusClusterPlus' for longitudinal data. The longitudinal data is
    clustered with flexible mixture models from 'flexmix', while the consensus
    matrices are hierarchically clustered as in 'ConsensusClusterPlus'. By using
    the flexibility from 'flexmix' and 'FactoMineR', one can use mixed data
    types for the clustering.
	"""
	
	homepage = "https://cellmapslab.github.io/longmixr/"
	cran = "longmixr" 

	version("1.0.0", md5="666cb318313973453f137efd6c5bd6db")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-consensusclusterplus", type=("build", "run"))
	depends_on("r-flexmix", type=("build", "run"))
	depends_on("r-statmatch", type=("build", "run"))
