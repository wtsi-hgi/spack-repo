# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPfica(RPackage):
	"""Independent Components Analysis Techniques for Functional Data

	Performs smoothed (and non-smoothed) principal/independent components analysis
  of functional data. Various functional pre-whitening approaches are implemented as 
  discussed in Vidal and Aguilera (2022) “Novel whitening approaches in functional 
  settings", <doi:10.1002/sta4.516>. Further whitening representations of functional 
  data can be derived in terms of a few principal components, providing an avenue 
  to explore hidden structures in low dimensional settings: see Vidal,
  Rosso and Aguilera (2021) “Bi-smoothed functional independent component 
  analysis for EEG artifact removal”, <doi:10.3390/math9111243>.  
	"""
	
	homepage = "https://github.com/m-vidal/pfica"
	cran = "pfica" 

	version("0.1.3", md5="2c512b09edfac8e2742338f4fa1ad0a5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-whitening", type=("build", "run"))
