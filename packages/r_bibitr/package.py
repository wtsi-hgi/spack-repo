# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBibitr(RPackage):
	"""R Wrapper for Java Implementation of BiBit

	A simple R wrapper for the Java BiBit algorithm from "A
    biclustering algorithm for extracting bit-patterns from binary datasets"
    from Domingo et al. (2011) <DOI:10.1093/bioinformatics/btr464>. An simple adaption for the BiBit algorithm which allows noise in the biclusters is also introduced as well as a function to guide the algorithm towards given (sub)patterns. Further, a workflow to derive noisy biclusters from discoverd larger column patterns is included as well.
	"""
	
	cran = "BiBitR" 

	version("0.3.1", md5="1f60bce8f414478aa5c4c2c0035ab69b")

	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-randomcolor", type=("build", "run"))
	depends_on("r-biclust", type=("build", "run"))
	depends_on("openjdk", type=("build", "link", "run"))
