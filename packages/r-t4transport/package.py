# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RT4transport(RPackage):
	"""Tools for Computational Optimal Transport

	Transport theory has seen much success in many fields of statistics and machine learning. We provide a variety of algorithms to compute Wasserstein distance, barycenter, and others. See Peyré and Cuturi (2019) <doi:10.1561/2200000073> for the general exposition to the study of computational optimal transport.
	"""
	
	cran = "T4transport" 

	version("0.1.2", md5="1649295eeb79be8b798ca588a3b2f60b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cvxr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
