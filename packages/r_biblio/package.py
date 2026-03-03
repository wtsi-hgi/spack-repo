# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiblio(RPackage):
	"""Interacting with BibTeX Databases

	Reading and writing BibTeX files using data frames in R sessions.
	"""
	
	homepage = "https://kamapu.github.io/biblio/"
	cran = "biblio" 

	version("0.0.8", md5="5bfd9346e84c6019ae3c63204210dee2")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-yamlme", type=("build", "run"))
	depends_on("pandoc@1.14:", type=("build", "link", "run"))
