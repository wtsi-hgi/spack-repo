# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROntologysimilarity(RPackage):
	"""Calculating Ontological Similarities

	Calculate similarity between ontological terms and sets of ontological terms based on term information content and assess statistical significance of similarity in the context of a collection of terms sets - Greene et al. 2017 <doi:10.1093/bioinformatics/btw763>.
	"""
	
	cran = "ontologySimilarity" 

	version("2.7", md5="822cf4c2e980595be40ae54843e82095")
	version("2.5", md5="316eca09a009b20c4cb65d4ab7d2ba27")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ontologyindex@2:", type=("build", "run"))
