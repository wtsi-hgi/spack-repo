# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDove(RPackage):
	"""Durability of Vaccine Efficacy

	Implements maximum likelihood methods for 
    evaluating the durability of vaccine efficacy in a randomized, 
    placebo-controlled clinical trial with staggered enrollment of participants 
    and potential crossover of placebo recipients before the end of the trial. 
    Lin, D. Y., Zeng, D., and Gilbert, P. B. (2021) 
    <doi:10.1093/cid/ciab226>
    and 
    Lin, D. Y., Gu, Y., Zeng, D., Janes, H. E., and Gilbert, P. B. (2021) 
    <doi:10.1093/cid/ciab630>. 
	"""
	
	cran = "DOVE" 

	version("1.10", md5="2471bb69f8549e33e559443a073b15ce")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
