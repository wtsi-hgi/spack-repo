# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNgchm(RPackage):
	"""Next Generation Clustered Heat Maps

	Next-Generation Clustered Heat Maps (NG-CHMs) allow for
    dynamic exploration of heat map data in a web browser. 'NGCHM' allows
    users to create both stand-alone HTML files containing a
    Next-Generation Clustered Heat Map, and .ngchm files to view in the
    NG-CHM viewer. See Ryan MC, Stucky M, et al (2020)
    <doi:10.12688/f1000research.20590.2> for more details.
	"""
	
	homepage = "https://md-anderson-bioinformatics.github.io/NGCHM-R/"
	cran = "NGCHM" 

	version("1.0.1", md5="59ebbe7552f8ce2da3c3c52029f9b8d8")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-logger@0.2:", type=("build", "run"))
	depends_on("r-tsvio", type=("build", "run"))
	depends_on("java@1.8:", type=("build", "link", "run"))
	depends_on("git", type=("build", "link", "run"))
