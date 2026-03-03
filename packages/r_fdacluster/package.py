# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFdacluster(RPackage):
	"""Joint Clustering and Alignment of Functional Data

	Implementations of the k-means, hierarchical agglomerative and 
    DBSCAN clustering methods for functional data which allows for jointly 
    aligning and clustering curves. It supports functional data defined on 
    one-dimensional domains but possibly evaluating in multivariate codomains. 
    It supports functional data defined in arrays but also via the 'fd' and 
    'funData' classes for functional data defined in the 'fda' and 'funData' 
    packages respectively. It currently supports shift, dilation and affine 
    warping functions for functional data defined on the real line and uses the 
    SRSF framework to handle boundary-preserving warping for functional data 
    defined on a specific interval. Main reference for the k-means algorithm: 
    Sangalli L.M., Secchi P., Vantini S., Vitelli V. (2010) "k-mean alignment 
    for curve clustering" <doi:10.1016/j.csda.2009.12.008>. Main reference for 
    the SRSF framework: Tucker, J. D., Wu, W., & Srivastava, A. (2013) 
    "Generative models for functional data using phase and amplitude separation" 
    <doi:10.1016/j.csda.2012.12.001>.
	"""
	
	homepage = "https://astamm.github.io/fdacluster/index.html"
	cran = "fdacluster" 

	version("0.3.0", md5="ce2fc4f630d20a44b427c5b45b051f29")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-dbscan", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fdasrvf", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
