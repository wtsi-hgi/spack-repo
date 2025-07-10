# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHierinf(RPackage):
	"""Hierarchical Inference

	Tools to perform hierarchical inference for one or multiple studies / data sets based on high-dimensional multivariate (generalised) linear models. A possible application is to perform hierarchical inference for GWA studies to find significant groups or single SNPs (if the signal is strong) in a data-driven and automated procedure. The method is based on an efficient hierarchical multiple testing correction and controls the FWER. The functions can easily be run in parallel.
	"""
	
	bioc = "hierinf" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/hierinf_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/hierinf/hierinf_1.20.0.tar.gz"]

	version("1.20.0", sha256="2edfb84d30e828e9eda025aab1808863f1c52bd30eb770f007e1c3e765440baa")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-fmsb", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
