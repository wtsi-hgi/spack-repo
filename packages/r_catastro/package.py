# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCatastro(RPackage):
	"""Interface to the API 'Sede Electronica Del Catastro'

	Access public spatial data available under the 'INSPIRE'
    directive. Tools for downloading references and addresses of
    properties, as well as map images.
	"""
	
	homepage = "https://ropenspain.github.io/CatastRo/"
	cran = "CatastRo" 

	version("0.3.0", md5="688352ea59215d0e63e98da0bdbc1432")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-mapspain@0.7:", type=("build", "run"))
	depends_on("r-rappdirs@0.3:", type=("build", "run"))
	depends_on("r-sf@1:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
