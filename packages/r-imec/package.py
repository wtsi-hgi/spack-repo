# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImec(RPackage):
	"""Ising Model of Explanatory Coherence

	
    Theories are one of the most important tools of science. Although psychologists discussed problems of theory in their discipline for a long time, weak theories are still widespread in most subfields. 
    One possible reason for this is that psychologists lack the tools to systematically assess the quality of their theories. 
    Previously a computational model for formal theory evaluation based on the concept of explanatory coherence was developed (Thagard, 1989, <doi:10.1017/S0140525X00057046>). 
    However, there are possible improvements to this model and it is not available in software that psychologists typically use. 
    Therefore, a new implementation of explanatory coherence based on the Ising model is available in this R-package.
	"""
	
	cran = "IMEC" 

	version("0.2.0", md5="525dd5c2f3232d53118ca7c1e8af0fb2")

	depends_on("r-isingsampler", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-qgraph", type=("build", "run"))
