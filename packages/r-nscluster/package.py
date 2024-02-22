# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNscluster(RPackage):
	"""Simulation and Estimation of the Neyman-Scott Type Spatial
Cluster Models

	Simulation and estimation for Neyman-Scott spatial cluster point
 process models and their extensions, based on the methodology in Tanaka, Ogata,
 and Stoyan (2008) <doi:10.1002/bimj.200610339>. To estimate parameters by the
 simplex method, parallel computation using 'OpenMP' application programming
 interface is available. For more details see Tanaka, Saga and Nakano
 <doi:10.18637/jss.v098.i06>.
	"""
	
	cran = "NScluster" 

	version("1.3.6-1", md5="b93f3559b361e0de6a466716c51ef2a1")

	depends_on("r@3:", type=("build", "run"))
