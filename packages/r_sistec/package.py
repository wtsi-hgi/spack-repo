# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSistec(RPackage):
	"""Tools to Analyze 'Sistec' Datasets

	The Brazilian system for diploma registration and validation on technical and superior
    courses are managing by 'Sistec' platform, see <https://sistec.mec.gov.br/>. This package provides 
    tools for Brazilian institutions to update the student's registration and make data analysis 
    about their situation, retention and drop out.
	"""
	
	homepage = "https://github.com/r-ifpe/sistec"
	cran = "sistec" 

	version("0.2.0", md5="7ba8b965689c3ae3df57aa62616d91b3")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
