# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbiopaxparser(RPackage):
	"""Parses BioPax files and represents them in R

	Parses BioPAX files and represents them in R, at the moment BioPAX level 2 and level 3 are supported.
	"""
	
	homepage = "https://github.com/frankkramer-lab/rBiopaxParser"
	bioc = "rBiopaxParser" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/rBiopaxParser_2.42.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/rBiopaxParser/rBiopaxParser_2.42.0.tar.gz"]

    version("2.48.0", tag="RELEASE_3_21")
	version("2.42.0", sha256="275cb296a6e9d262a2c853d85c0954fcf72a87197b482adfbb4c8e045346caff")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
