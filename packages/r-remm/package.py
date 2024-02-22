# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRemm(RPackage):
	"""Extensible Markov Model for Modelling Temporal Relationships
Between Clusters

	Implements TRACDS (Temporal Relationships 
    between Clusters for Data Streams), a generalization of 
    Extensible Markov Model (EMM). TRACDS adds a temporal or order model
    to data stream clustering by superimposing a dynamically adapting
    Markov Chain. Also provides an implementation of EMM (TRACDS on top of tNN 
    data stream clustering). Development of this 
    package was supported in part by NSF IIS-0948893 and R21HG005912 from 
    the National Human Genome Research Institute. Hahsler and Dunham (2010) <doi:10.18637/jss.v035.i05>.
	"""
	
	homepage = "https://github.com/mhahsler/rEMM"
	cran = "rEMM" 

	version("1.2.0", md5="b5b8b5c82e123438845d3d5cd4322bf8")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-proxy@0.4.7:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-stream", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-clustergeneration", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
