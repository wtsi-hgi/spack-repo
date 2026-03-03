# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLinkagemapview(RPackage):
	"""Plot Linkage Group Maps with Quantitative Trait Loci

	Produces high resolution, publication ready linkage maps
    and quantitative trait loci maps. Input can be output from 'R/qtl',
    simple text or comma delimited files. Output is currently
    a portable document file.
	"""
	
	homepage = "https://github.com/louellette/LinkageMapView"
	cran = "LinkageMapView" 

	version("2.1.2", md5="3dfe7d55376dc43f7a01f1c11bf70933")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-qtl@1.39.5:", type=("build", "run"))
	depends_on("r-plotrix@3.6.3:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
