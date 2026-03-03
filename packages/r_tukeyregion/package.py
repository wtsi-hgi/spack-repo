# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTukeyregion(RPackage):
	"""Tukey Region and Median

	Tukey regions are polytopes in the Euclidean space, viz. 
    upper-level sets of the Tukey depth function on given data. The bordering 
    hyperplanes of a Tukey region are computed as well as its vertices, facets, 
    centroid, and volume. In addition, the Tukey median set, which is the 
    non-empty Tukey region having highest depth level, and its barycenter 
    (= Tukey median) are calculated. Tukey regions are visualized in dimension 
    two and three. For details see Liu, Mosler, and Mozharovskyi 
    (2019, <doi:10.1080/10618600.2018.1546595>). See file LICENSE.note for 
    additional license information.
	"""
	
	cran = "TukeyRegion" 

	version("0.1.6.3", md5="412f2a4a391e8263e40984cbbff9a8d2")

	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-ddalpha", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-bfp", type=("build", "run"))
	depends_on("r-rglpk", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
