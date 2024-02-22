# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDynatree(RPackage):
	"""Dynamic Trees for Learning and Design

	Inference by sequential Monte Carlo for 
  dynamic tree regression and classification models
  with hooks provided for sequential design and optimization, 
  fully online learning with drift, variable selection, and 
  sensitivity analysis of inputs.  Illustrative 
  examples from the original dynamic trees paper 
  (Gramacy, Taddy & Polson (2011); <doi:10.1198/jasa.2011.ap09769>) are facilitated
  by demos in the package; see demo(package="dynaTree").
	"""
	
	homepage = "https://bobby.gramacy.com/r_packages/dynaTree/"
	cran = "dynaTree" 

	version("1.2-16", md5="6354809d65eb21249422a7f29427ce89")

	depends_on("r@2.14:", type=("build", "run"))
