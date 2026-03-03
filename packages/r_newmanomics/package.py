# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNewmanomics(RPackage):
	"""Extending the Newman Studentized Range Statistic to
Transcriptomics

	Extends the classical Newman studentized range statistic
  in various ways that can be applied to genome-scale transcriptomic
  or other expression data.
	"""
	
	homepage = "http://oompa.r-forge.r-project.org/"
	cran = "NewmanOmics" 

	version("1.0.10", md5="fa4186411854610e54339e48361398a9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-oompabase", type=("build", "run"))
