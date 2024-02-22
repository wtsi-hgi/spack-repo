# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRefinr(RPackage):
	"""Cluster and Merge Similar Values Within a Character Vector

	These functions take a character vector as input, identify and 
  cluster similar values, and then merge clusters together so their values 
  become identical. The functions are an implementation of the key collision 
  and ngram fingerprint algorithms from the open source tool Open Refine 
  <https://openrefine.org/>. More info on key collision and ngram fingerprint 
  can be found here <https://openrefine.org/docs/technical-reference/clustering-in-depth>.
	"""
	
	homepage = "https://github.com/ChrisMuir/refinr"
	cran = "refinr" 

	version("0.3.3", md5="59e6a1f29d0af9b4d59d4c6ac4cc4984")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-stringdist@0.9.5.1:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
