# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNodesub(RPackage):
	"""Simulate DNA Alignments Using Node Substitutions

	Simulate DNA sequences for the node substitution model.
    In the node substitution model, substitutions accumulate additionally 
    during a speciation event, providing a potential mechanistic explanation for 
    substitution rate variation. This package provides tools to simulate
    such a process, simulate a reference process with only substitutions along
    the branches, and provides tools to infer phylogenies from alignments. More
    information can be found in Janzen (2021) <doi:10.1093/sysbio/syab085>.
	"""
	
	homepage = "https://github.com/thijsjanzen/nodeSub"
	cran = "nodeSub" 

	version("1.2.8", md5="82a0ee618aed475be403f0b0a139c1eb")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-phangorn", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ddd", type=("build", "run"))
	depends_on("r-rmpfr", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-phylobase", type=("build", "run"))
	depends_on("r-geiger", type=("build", "run"))
	depends_on("r-beautier", type=("build", "run"))
	depends_on("r-beastier", type=("build", "run"))
	depends_on("r-tracerer", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-testit", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
