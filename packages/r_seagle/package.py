# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeagle(RPackage):
	"""Scalable Exact Algorithm for Large-Scale Set-Based
Gene-Environment Interaction Tests

	
    The explosion of biobank data offers immediate opportunities for 
    gene-environment (GxE) interaction studies of complex diseases because of the 
    large sample sizes and rich collection in genetic and non-genetic information. 
    However, the extremely large sample size also introduces new computational 
    challenges in GxE assessment, especially for set-based GxE variance component (VC) 
    tests, a widely used strategy to boost overall GxE signals and to evaluate the 
    joint GxE effect of multiple variants from a biologically meaningful unit 
    (e.g., gene). 
    We present 'SEAGLE', a Scalable Exact AlGorithm for Large-scale Set-based 
    GxE tests, to permit GxE VC test scalable to biobank data. 'SEAGLE' employs modern 
    matrix computations to achieve the same “exact” results as the original GxE VC 
    tests, and does not impose additional assumptions nor relies on approximations. 
    'SEAGLE' can easily accommodate sample sizes in the order of 10^5, is implementable 
    on standard laptops, and does not require specialized equipment. 
    The accompanying manuscript for this package can be found at Chi, Ipsen, Hsiao, 
    Lin, Wang, Lee, Lu, and Tzeng. (2021+) <arXiv:2105.03228>.
	"""
	
	homepage = "https://github.com/jocelynchi/SEAGLE"
	cran = "SEAGLE" 

	version("1.0.1", md5="6d13d3cdd0c7a603f94fe9339859759a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-compquadform", type=("build", "run"))
