# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUseful(RPackage):
	"""A Collection of Handy, Useful Functions

	A set of little functions that have been found useful to do little
    odds and ends such as plotting the results of K-means clustering, substituting
    special text characters, viewing parts of a data.frame, constructing formulas
    from text and building design and response matrices.
	"""
	
	homepage = "https://github.com/jaredlander/useful"
	cran = "useful" 

	version("1.2.6.1", md5="d777eea81ce19703a04dc5524be2fa88")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr@0.5:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr@0.1:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
