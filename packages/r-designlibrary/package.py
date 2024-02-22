# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDesignlibrary(RPackage):
	"""Library of Research Designs

	
    A simple interface to build designs using the package 'DeclareDesign'. 
    In one line of code, users can specify the parameters of individual 
    designs and diagnose their properties. The designers can also be used 
    to compare performance of a given design across a range of combinations 
    of parameters, such as effect size, sample size, and assignment probabilities.
	"""
	
	homepage = "https://declaredesign.org/r/designlibrary/"
	cran = "DesignLibrary" 

	version("0.1.10", md5="8ad45e9d10d95aadfed6343bc3f83300")

	depends_on("r-declaredesign@0.17:", type=("build", "run"))
	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-randomizr@0.16.1:", type=("build", "run"))
	depends_on("r-fabricatr@0.8:", type=("build", "run"))
	depends_on("r-estimatr@0.16:", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
