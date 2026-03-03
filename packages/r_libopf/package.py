# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLibopf(RPackage):
	"""Design of Optimum-Path Forest Classifiers

	The 'LibOPF' is a framework to develop pattern recognition techniques based on optimum-path forests (OPF), João P. Papa and Alexandre X. Falcão (2008) <doi:10.1007/978-3-540-89639-5_89>, with methods for supervised learning and data clustering.
	"""
	
	homepage = "https://github.com/RafaelJM/LibOPF-in-R"
	cran = "LibOPF" 

	version("2.6.2", md5="ed51117d3b91289f7ce31613862a1e48")

