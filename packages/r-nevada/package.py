# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNevada(RPackage):
	"""Network-Valued Data Analysis

	A flexible statistical framework for network-valued data analysis. 
    It leverages the complexity of the space of distributions on graphs by using 
    the permutation framework for inference as implemented in the 'flipr' package. 
    Currently, only the two-sample testing problem is covered and generalization 
    to k samples and regression will be added in the future as well. It is a 
    4-step procedure where the user chooses a suitable representation of the 
    networks, a suitable metric to embed the representation into a metric space, 
    one or more test statistics to target specific aspects of the distributions 
    to be compared and a formula to compute the permutation p-value. Two types 
    of inference are provided: a global test answering whether there is a 
    difference between the distributions that generated the two samples and a 
    local test for localizing differences on the network structure. The latter 
    is assumed to be shared by all networks of both samples. References: Lovato, 
    I., Pini, A., Stamm, A., Vantini, S. (2020) "Model-free two-sample test for 
    network-valued data" <doi:10.1016/j.csda.2019.106896>; Lovato, I., Pini, A., 
    Stamm, A., Taquet, M., Vantini, S. (2021) "Multiscale null hypothesis 
    testing for network-valued data: Analysis of brain networks of patients with 
    autism" <doi:10.1111/rssc.12463>.
	"""
	
	homepage = "https://astamm.github.io/nevada/"
	cran = "nevada" 

	version("0.2.0", md5="748c810804bd7e1936b37a2e47804e79")

	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-flipr", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-tsne", type=("build", "run"))
	depends_on("r-umap", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-rgeomstats", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
