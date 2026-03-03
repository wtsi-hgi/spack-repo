# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScperturbr(RPackage):
	"""E-Statistics for Seurat Objects

	R version of 'scperturb' tool for single-cell perturbation 
    analysis. Contains wrappers for performing E-statistics for Seurat objects. 
    More details on the method can be found in Peidli et al. (2023) 
    <doi:10.1101/2022.08.20.504663> and in Székely and Rizzo (2004).
	"""
	
	homepage = "https://github.com/sanderlab/scPerturb/tree/master/package_r"
	cran = "scperturbR" 

	version("0.1.0", md5="bb5eaa8737156ee85d47dcabc5d6f142")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rdist", type=("build", "run"))
	depends_on("r-energy", type=("build", "run"))
