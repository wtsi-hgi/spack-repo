# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSid(RPackage):
	"""Structural Intervention Distance

	The code computes the structural intervention distance (SID) between a true directed acyclic graph (DAG) and an estimated DAG. Definition and details about the implementation can be found in J. Peters and P. Bühlmann: "Structural intervention distance (SID) for evaluating causal graphs", Neural Computation 27, pages 771-799, 2015  <doi:10.1162/NECO_a_00708>.
	"""
	
	homepage = "https://github.com/fkgruber/SID_cran"
	cran = "SID" 

	version("1.1", md5="365acac1b14f5d4d2f2e7e0233678415")

	depends_on("r-pcalg", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rbgl", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
