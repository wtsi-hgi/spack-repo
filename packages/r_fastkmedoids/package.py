# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastkmedoids(RPackage):
	"""Faster K-Medoids Clustering Algorithms: FastPAM, FastCLARA,
FastCLARANS

	R wrappers of C++ implementation of Faster K-Medoids clustering algorithms (FastPAM, FastCLARA and FastCLARANS) proposed in Erich Schubert, Peter J. Rousseeuw 2019 <doi:10.1007/978-3-030-32047-8_16>.
	"""
	
	cran = "fastkmedoids" 

	version("1.2", md5="7c8a9d400997fbddafcdb5efbb3ea03f")

	depends_on("r-rcpp", type=("build", "run"))
