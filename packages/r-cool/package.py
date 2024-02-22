# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCool(RPackage):
	"""Causes of Outcome Learning

	Implementing the computational phase of the Causes of Outcome Learning approach as described in Rieckmann, Dworzynski, Arras, Lapuschkin, Samek, Arah, Rod, Ekstrom. 2022. Causes of outcome learning: A causal inference-inspired machine learning approach to disentangling common combinations of potential causes of a health outcome. International Journal of Epidemiology <doi:10.1093/ije/dyac078>. The optional 'ggtree' package can be obtained through Bioconductor.
	"""
	
	homepage = "https://bioconductor.org"
	cran = "CoOL" 

	version("1.1.2", md5="f6f20de2f603e247f26ca944d942d033")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-mltools", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-clustgeo", type=("build", "run"))
	depends_on("r-wesanderson", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
