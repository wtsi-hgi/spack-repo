# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTopicdoc(RPackage):
	"""Topic-Specific Diagnostics for LDA and CTM Topic Models

	Calculates topic-specific diagnostics (e.g. mean token length, exclusivity) for 
    Latent Dirichlet Allocation and Correlated Topic Models fit using the 'topicmodels' package.
    For more details, see Chapter 12 in Airoldi et al. (2014, ISBN:9781466504080), 
    pp 262-272 Mimno et al. (2011, ISBN:9781937284114), and Bischof et al. (2014) <arXiv:1206.4631v1>.
	"""
	
	homepage = "https://github.com/doug-friedman/topicdoc"
	cran = "topicdoc" 

	version("0.1.1", md5="3d05e8278bfbdc2241531593dd35bbdb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
	depends_on("r-topicmodels", type=("build", "run"))
