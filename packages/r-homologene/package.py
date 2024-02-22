# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHomologene(RPackage):
	"""Quick Access to Homologene and Gene Annotation Updates

	A wrapper for the homologene database by the National Center for
    Biotechnology Information ('NCBI'). It allows searching for gene homologs across 
    species. Data in this package can be found at <ftp://ftp.ncbi.nih.gov/pub/HomoloGene/build68/>.
    The package also includes an updated version of the homologene database where 
    gene identifiers and symbols are replaced with their latest (at the time of
    submission) version and functions to fetch latest annotation data to keep updated.
	"""
	
	homepage = "https://github.com/oganm/homologene"
	cran = "homologene" 

	version("1.4.68.19.3.27", md5="869cfcac341b7109d765fb3621cbca13")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-dplyr@0.7.4:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-purrr@0.2.5:", type=("build", "run"))
	depends_on("r-readr@1.3.1:", type=("build", "run"))
	depends_on("r-r-utils@2.8:", type=("build", "run"))
