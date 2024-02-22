# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPreprocess(RPackage):
	"""Basic Functions for Pre-Processing Microarrays

	Provides classes to pre-process microarray gene
  expression data as part of the OOMPA collection of packages
  described at <http://oompa.r-forge.r-project.org/>.
	"""
	
	homepage = "http://oompa.r-forge.r-project.org/"
	cran = "PreProcess" 

	version("3.1.7", md5="bb2ae2f3e089d66cf7509207f90ccb03")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-oompabase@3:", type=("build", "run"))
