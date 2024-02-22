# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROompadata(RPackage):
	"""Data to Illustrate OOMPA Algorithms

	This is a data-only package to provide example data for
  other packages that are part of the "Object-Oriented Microrray and
  Proteomics Analysis" suite of packages. These are described in more
  detail at the package URL.
	"""
	
	homepage = "http://oompa.r-forge.r-project.org/"
	cran = "oompaData" 

	version("3.1.3", md5="abc4fbe9d5e709991115035d30abfbb8")

	depends_on("r@3:", type=("build", "run"))
