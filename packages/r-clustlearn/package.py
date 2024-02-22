# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClustlearn(RPackage):
	"""Learn Clustering Techniques Through Examples and Code

	Clustering methods, which (if asked) can provide step-by-step
    explanations of the algorithms used, as described in Ezugwu et. al., (2022)
    <doi:10.1016/j.engappai.2022.104743>; and datasets to test them on, which
    highlight the strengths and weaknesses of each technique, as presented in
    the clustering section of 'scikit-learn' (Pedregosa et al., 2011)
    <https://jmlr.csail.mit.edu/papers/v12/pedregosa11a.html>.
	"""
	
	homepage = "https://github.com/Ediu3095/clustlearn"
	cran = "clustlearn" 

	version("1.0.0", md5="4464c7491e9597714cfc45167e1d6f9c")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-proxy@0.4.27:", type=("build", "run"))
	depends_on("r-cli@3.6.1:", type=("build", "run"))
