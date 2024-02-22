# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExperdesign(RPackage):
	"""Design Experiments for Batches

	Distributes samples in batches while making batches
    homogeneous according to their description. Allows for an arbitrary
    number of variables, both numeric and categorical. For quality control
    it provides functions to subset a representative sample.
	"""
	
	homepage = "https://experdesign.llrs.dev"
	cran = "experDesign" 

	version("0.3.0", md5="5e0ccdcf6f28f081b2cb5f8584f518ed")

	depends_on("r@3.5:", type=("build", "run"))
