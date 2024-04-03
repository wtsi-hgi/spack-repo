# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMpae(RPackage):
	"""Metodos Predictivos de Aprendizaje Estadistico (Statistical
Learning Predictive Methods)

	Functions and datasets used in the book: Fernandez-Casal, R., 
    Costa, J. and Oviedo-de la Fuente, M. (2024) "Metodos predictivos de 
    aprendizaje estadistico" <https://rubenfcasal.github.io/aprendizaje_estadistico/>.
	"""
	
	homepage = "https://github.com/rubenfcasal/mpae"
	cran = "mpae" 

	version("0.1.2", md5="b3f2aaa004331620e75a087d4293590c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-rcmdrmisc", type=("build", "run"))
