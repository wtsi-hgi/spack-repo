# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDifconet(RPackage):
	"""Differential Coexpressed Networks

	Estimation of DIFferential COexpressed NETworks using diverse and user metrics.
			 This package is basically used for three functions related to the estimation
			 of differential coexpression. 
			 First, to estimate differential coexpression where
			 the coexpression is estimated, by default, by Spearman correlation. For this,
			 a metric to compare two correlation distributions is needed. The package includes
			 6 metrics. Some of them needs a threshold. A new metric can also be specified as
			 a user function with specific parameters (see difconet.run). The significance is
			 be estimated by permutations.
			 Second, to generate datasets with controlled differential correlation data. This 
			 is done by either adding noise, or adding specific correlation structure.
			 Third, to show the results of differential correlation analyses. Please see
			 <http://bioinformatica.mty.itesm.mx/difconet> for further information.
	"""
	
	homepage = "http://bioinformatica.mty.itesm.mx/difconet"
	cran = "difconet" 

	version("1.0-4", md5="034571603b65964cf8cc8d9abed5340a")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
