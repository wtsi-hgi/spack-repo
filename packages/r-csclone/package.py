# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCsclone(RPackage):
	"""Bayesian Nonparametric Modeling in R

	Germline and somatic locus data which contain the total read depth and B allele 
    read depth using Bayesian model (Dirichlet Process) to cluster. Meanwhile, the cluster 
    model can deal with the SNVs mutation and the CNAs mutation.
	"""
	
	cran = "CSclone" 

	version("1.0", md5="01dc949405676bbdb4983c4c3d4639b8")

	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-mcclust", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-dnacopy", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
