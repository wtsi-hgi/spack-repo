# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReadsparse(RPackage):
	"""Read and Write Sparse Matrices in 'SVMLight' and 'LibSVM'
Formats

	Read and write labelled sparse matrices in text format as used by
    software such as 'SVMLight', 'LibSVM', 'ThunderSVM', 'LibFM', 'xLearn', 'XGBoost', 'LightGBM',
    and others. Supports labelled data for regression, classification (binary, multi-class, multi-label),
    and ranking (with 'qid' field), and can handle header metadata and comments in files.
	"""
	
	homepage = "https://github.com/david-cortes/readsparse"
	cran = "readsparse" 

	version("0.1.5-6", md5="f4fe0469cff6ce07c2538202a178a1da")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
