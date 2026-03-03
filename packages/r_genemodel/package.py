# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenemodel(RPackage):
	"""Gene Model Plotting in R

	Using simple input, this package creates plots of gene models. Users can create plots of alternatively spliced gene variants and the positions of mutations and other gene features.
	"""
	
	homepage = "https://github.com/greymonroe/genemodel"
	cran = "genemodel" 

	version("1.1.0", md5="754370477e74880f2606e7f74dcc169c")

	depends_on("r@3.2.5:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
