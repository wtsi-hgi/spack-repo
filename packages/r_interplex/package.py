# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInterplex(RPackage):
	"""Coercion Methods for Simplicial Complex Data Structures

	Computational topology, which enables topological data analysis
    (TDA), makes pervasive use of abstract mathematical objects called
    simplicial complexes; see Edelsbrunner and Harer (2010)
    <doi:10.1090/mbk/069>.
    Several R packages and other software libraries used through an R interface
    construct and use data structures that represent simplicial complexes,
    including mathematical graphs viewed as 1-dimensional complexes.
    This package provides coercers (converters) between these data structures.
    Currently supported structures are complete lists of simplices as used by
    'TDA'; the simplex trees of Boissonnat and Maria (2014)
    <doi:10.1007/s00453-014-9887-3> as implemented in 'simplextree' and in
    Python GUDHI (by way of 'reticulate'); and the graph classes of 'igraph' and
    'network', by way of the 'intergraph' package.
	"""
	
	homepage = "https://github.com/tdaverse/interplex"
	cran = "interplex" 

	version("0.1.2", md5="9d94b8bc5c638ae163876013811c6cb8")

	depends_on("r-intergraph", type=("build", "run"))
	depends_on("r-igraph@0.6.0:", type=("build", "run"))
	depends_on("r-network@1.4.2:", type=("build", "run"))
	depends_on("r-simplextree@0.9.1:", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
