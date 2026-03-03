# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpacefillr(RPackage):
	"""Space-Filling Random and Quasi-Random Sequences

	Generates random and quasi-random space-filling sequences. Supports the following sequences: 'Halton', 'Sobol', 'Owen'-scrambled 'Sobol',  'Owen'-scrambled 'Sobol' with errors distributed as blue noise, progressive jittered, progressive multi-jittered ('PMJ'), 'PMJ' with blue noise, 'PMJ02', and 'PMJ02' with blue noise. Includes a 'C++' 'API'. Methods derived from "Constructing Sobol sequences with better two-dimensional projections" (2012) <doi:10.1137/070709359> S. Joe and F. Y. Kuo, "Progressive Multi-Jittered Sample Sequences" (2018) <https://graphics.pixar.com/library/ProgressiveMultiJitteredSampling/paper.pdf> Christensen, P., Kensler, A. and Kilpatrick, C., and "A Low-Discrepancy Sampler that Distributes Monte Carlo Errors as a Blue Noise in Screen Space" (2019) E. Heitz, B. Laurent, O. Victor, C. David and I. Jean-Claude, <doi:10.1145/3306307.3328191>. 
	"""
	
	homepage = "https://github.com/tylermorganwall/spacefillr"
	cran = "spacefillr" 

	version("0.3.2", md5="15134937642c29ace86b414446bc130f")

	depends_on("r-rcpp", type=("build", "run"))
