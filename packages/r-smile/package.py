# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmile(RPackage):
	"""Spatial Misalignment: Interpolation, Linkage, and Estimation

	Provides functions to estimate, predict and interpolate areal
        data. For estimation and prediction we assume areal data is an average
        of an underlying continuous spatial process as in Moraga et
        al. (2017) <doi:10.1016/j.spasta.2017.04.006>, Johnson et al. (2020)
        <doi:10.1186/s12942-020-00200-w>, and Wilson and Wakefield (2020)
        <doi:10.1093/biostatistics/kxy041>. The interpolation methodology is
        (mostly) based on Goodchild and Lam (1980, ISSN:01652273).
	"""
	
	homepage = "https://lcgodoy.me/smile/"
	cran = "smile" 

	version("1.0.4.1", md5="89930de022f768ab573359eb452b7631")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("gdal@2.0.1:", type=("build", "link", "run"))
	depends_on("geos@3.4.0:", type=("build", "link", "run"))
	depends_on("proj@4.8.0:", type=("build", "link", "run"))
