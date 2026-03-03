# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetworkabc(RPackage):
	"""Network Reverse Engineering with Approximate Bayesian
Computation

	We developed an inference tool based on approximate Bayesian computation to decipher network data and assess the strength of the inferred links between network's actors. It is a new multi-level approximate Bayesian computation (ABC) approach. At the first level, the method captures the global properties of the network, such as a scale-free structure and clustering coefficients, whereas the second level is targeted to capture local properties, including the probability of each couple of genes being linked. Up to now, Approximate Bayesian Computation (ABC) algorithms have been scarcely used in that setting and, due to the computational overhead, their application was limited to a small number of genes. On the contrary, our algorithm was made to cope with that issue and has low computational cost. It can be used, for instance, for elucidating gene regulatory network, which is an important step towards understanding the normal cell physiology and complex pathological phenotype. Reverse-engineering consists in using gene expressions over time or over different experimental conditions to discover the structure of the gene network in a targeted cellular process. The fact that gene expression data are usually noisy, highly correlated, and have high dimensionality explains the need for specific statistical methods to reverse engineer the underlying network. 
	"""
	
	homepage = "https://fbertran.github.io/networkABC/"
	cran = "networkABC" 

	version("0.8-1", md5="95dc66dfc147ffcd66af435534e977ba")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-sna", type=("build", "run"))
