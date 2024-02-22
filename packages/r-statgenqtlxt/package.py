# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStatgenqtlxt(RPackage):
	"""Multi-Trait and Multi-Trial Genome Wide Association Studies

	Fast multi-trait and multi-trail Genome Wide Association Studies 
    (GWAS) following the method described in Zhou and Stephens. (2014), 
    <doi:10.1038/nmeth.2848>. One of a series of statistical genetic packages 
    for streamlining the analysis of typical plant breeding experiments 
    developed by Biometris.
	"""
	
	cran = "statgenQTLxT" 

	version("1.0.2", md5="5c06edfd6bc2433555527684d0d0f9da")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-sommer@4.2:", type=("build", "run"))
	depends_on("r-statgengwas@1.0.9:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
