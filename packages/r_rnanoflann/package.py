# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnanoflann(RPackage):
	"""Extremely Fast Nearest Neighbor Search

	Finds the k nearest neighbours for every point in a given dataset using Jose Luis' 'nanoflann' library. There is support for exact searches, fixed radius searches with 'kd' trees and two distances, the 'Euclidean' and 'Manhattan'. For more information see <https://github.com/jlblancoc/nanoflann>. Also, the 'nanoflann' library is exported and ready to be used via the linking to mechanism.
	"""
	
	homepage = "https://github.com/ManosPapadakis95/Rnanoflann"
	cran = "Rnanoflann" 

	version("0.0.2", md5="b5e3eea867f4ad4fc22409a40f1e1874")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
