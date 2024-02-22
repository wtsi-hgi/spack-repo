# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHypothesisr(RPackage):
	"""Wrapper for the 'Hypothes.is' Web Annotation Service

	Interact with the application programming interface for the web
    annotation service 'Hypothes.is' (See <http://hypothes.is> for more
    information.) Allows users to download data about public annotations, and
    create, retrieve, update, and delete their own annotations.
	"""
	
	homepage = "https://github.com/mdlincoln/hypothesisr"
	cran = "hypothesisr" 

	version("0.1.1", md5="86b681e3d853852844d64c11fbbc7a8a")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
