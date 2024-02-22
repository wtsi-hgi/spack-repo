# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPipeliner(RPackage):
	"""Machine Learning Pipelines for R

	A framework for defining 'pipelines' of functions for applying data transformations, 
  model estimation and inverse-transformations, resulting in predicted value generation (or 
  model-scoring) functions that automatically apply the entire pipeline of functions required to go
  from input to predicted output.
	"""
	
	homepage = "https://github.com/alexioannides/pipeliner"
	cran = "pipeliner" 

	version("0.1.1", md5="2dd4968610b5aabc4ca3018bff083659")

