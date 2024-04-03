# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIlsm(RPackage):
	"""Analyze Inter-Layer Structure of Multilayer Ecological Network

	
    In view of the analysis of the structural characteristics of the multilayer network has been complete, however, there is still a lack of a unified operation that can quickly obtain the corresponding characteristics of the multilayer network. 
    To solve this insufficiency, 'ILSM' was designed for supporting calculating such metrics of multilayer network by functions of this R package.
	"""
	
	cran = "ILSM" 

	version("1.0.1", md5="7ce26e193e6b58a35057cf4873b53738")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
