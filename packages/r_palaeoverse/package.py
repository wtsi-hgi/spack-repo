# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPalaeoverse(RPackage):
	"""Prepare and Explore Data for Palaeobiological Analyses

	Provides functionality to support data preparation and exploration for
  palaeobiological analyses, improving code reproducibility and accessibility. The
  wider aim of 'palaeoverse' is to bring the palaeobiological community together 
  to establish agreed standards. The package currently includes functionality for 
  data cleaning, binning (time and space), exploration, summarisation and 
  visualisation. Reference datasets (i.e. Geological Time Scales <https://stratigraphy.org/chart>)
  and auxiliary functions are also provided. Details can be found in:
  Jones et al., (2023) <doi: 10.1111/2041-210X.14099>.
	"""
	
	homepage = "https://palaeoverse.palaeoverse.org"
	cran = "palaeoverse" 

	version("1.2.1", md5="a4995450aa6953097b90345a7b1d76b5")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-h3jsr@1.3:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
