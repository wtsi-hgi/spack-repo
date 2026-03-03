# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRphosfate(RPackage):
	"""Soil and Chemical Substance Emission and Transport Model

	An enhanced version of the semi-empirical, spatially distributed
    emission and transport model PhosFate implemented in 'R' and 'C++'. It
    currently supports suspended solids (SS) and particulate phosphorus (PP). A
    major feature is the allocation of substance loads entering surface waters
    to their sources of origin, which is a basic requirement for the
    identification of critical source areas and in consequence a cost-effective
    implementation of mitigation measures. References: Hepp et al. (2022)
    <doi:10.1016/j.jenvman.2022.114514>; Hepp and Zessner (2019)
    <doi:10.3390/w11102161>; Kovacs (2013)
    <http://hdl.handle.net/20.500.12708/9468>.
	"""
	
	homepage = "https://gisler.github.io/RPhosFate/"
	cran = "RPhosFate" 

	version("1.0.4", md5="6f7928187f6c877718759a447f030780")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-raster@3.6.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
