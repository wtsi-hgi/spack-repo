# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDclear(RPackage):
	"""Distance Based Cell Lineage Reconstruction

	R codes for distance based cell lineage reconstruction. Our methods won both sub-challenges 2 and 3 of the Allen Institute Cell Lineage Reconstruction DREAM Challenge in 2020. 
        References: Gong et al. (2021) <doi:10.1016/j.cels.2021.05.008>, Gong et al. (2022) <doi:10.1186/s12859-022-04633-x>. 
	"""
	
	homepage = "https://github.com/ikwak2/DCLEAR"
	cran = "DCLEAR" 

	version("1.0.13", md5="9d8efd1b5eab75633367a01d41b596fd")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-tensorflow@2.2:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-phangorn", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rbayesianoptimization", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
