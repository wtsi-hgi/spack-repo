# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDaks(RPackage):
	"""Data Analysis and Knowledge Spaces

	Functions and an example dataset for the psychometric theory of
  knowledge spaces.  This package implements data analysis methods and
  procedures for simulating data and quasi orders and transforming different
  formulations in knowledge space theory.  See package?DAKS for an overview.
	"""
	
	homepage = "http://www.meb.edu.tum.de"
	cran = "DAKS" 

	version("2.1-3", md5="508f8c4f82786efc20c2dfd4ccddc204")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-relations", type=("build", "run"))
	depends_on("r-sets", type=("build", "run"))
