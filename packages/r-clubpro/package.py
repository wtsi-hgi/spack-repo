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
	
	homepage = "https://timbeechey.github.io/clubpro/"
	cran = "clubpro" 

	version("0.6.0", md5="5b4c9ed93970dd8bb80caf2246482578")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
