# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReusedata(RPackage):
	"""Reusable and reproducible Data Management

	ReUseData is an _R/Bioconductor_ software tool to provide a systematic and versatile approach for standardized and reproducible data management. ReUseData facilitates transformation of shell or other ad hoc scripts for data preprocessing into workflow-based data recipes. Evaluation of data recipes generate curated data files in their generic formats (e.g., VCF, bed). Both recipes and data are cached using database infrastructure for easy data management and reuse. Prebuilt data recipes are available through ReUseData portal ("https://rcwl.org/dataRecipes/") with full annotation and user instructions. Pregenerated data are available through ReUseData cloud bucket that is directly downloadable through "getCloudData()".
	"""
	
	homepage = "https://github.com/rworkflow/ReUseData"
	bioc = "ReUseData" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ReUseData_1.2.2.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ReUseData/ReUseData_1.2.2.tar.gz"]

	version("1.2.2", md5="c0041ec5d810d0d043c7375e04e78c06")

	depends_on("r-rcwl", type=("build", "run"))
	depends_on("r-rcwlpipelines", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-basilisk", type=("build", "run"))
