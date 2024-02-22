# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrthodr(RPackage):
	"""Semi-Parametric Dimension Reduction Models Using Orthogonality
Constrained Optimization

	Utilize an orthogonality constrained optimization algorithm of
    Wen & Yin (2013) <DOI:10.1007/s10107-012-0584-1> to solve a variety of
    dimension reduction problems in the semiparametric framework, such as
    Ma & Zhu (2012) <DOI:10.1080/01621459.2011.646925>, Ma & Zhu (2013) 
    <DOI:10.1214/12-AOS1072>, Sun, Zhu, Wang & Zeng (2019) <DOI:10.1093/biomet/asy064>
    and Zhou, Zhu & Zeng (2021) <DOI:10.1093/biomet/asaa087>. The package also
    implements some existing dimension reduction methods such as hMave by Xia, Zhang,
    & Xu (2010) <DOI:10.1198/jasa.2009.tm09372> and partial SAVE by Feng, Wen & Zhu (2013)
    <DOI:10.1080/01621459.2012.746065>. It also serves as a general purpose 
    optimization solver for problems with orthogonality constraints, i.e., in Stiefel 
    manifold. Parallel computing for approximating the gradient is enabled through 'OpenMP'.
	"""
	
	homepage = "https://github.com/teazrq/orthoDr"
	cran = "orthoDr" 

	version("0.6.7", md5="cfcf7afbe519963c9ca47de8059881ce")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-dr", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
