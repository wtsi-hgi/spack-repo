# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClubpro(RPackage):
	"""Classification Using Binary Procrustes Rotation

	Implements a classification method described by Grice (2011, ISBN:978-0-12-385194-9) using
    binary procrustes rotation; a simplified version of procrustes rotation.
	"""
	
	homepage = "https://github.com/timbeechey/clubpro"
	cran = "clubpro" 

	version("0.5.5", md5="a418f17a01f8b6751fb0dd1e5a2147ce")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
