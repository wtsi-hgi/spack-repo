# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeniebpc(RPackage):
	"""Project GENIE BioPharma Collaborative Data Processing Pipeline

	The American Association Research (AACR) Project 
    Genomics Evidence Neoplasia Information Exchange (GENIE) BioPharma 
    Collaborative represents a multi-year, multi-institution effort
    to build a pan-cancer repository of linked clinico-genomic data. 
    The genomic and clinical data are provided in multiple releases (separate
    releases for each cancer cohort with updates following data corrections), 
    which are stored on the data sharing platform 
    'Synapse' <https://www.synapse.org/>. 
    The 'genieBPC' package provides a seamless way to obtain the
    data corresponding to each release from 'Synapse' and to prepare
    datasets for analysis. 
	"""
	
	homepage = "https://genie-bpc.github.io/genieBPC/"
	cran = "genieBPC" 

	version("1.1.1", md5="65b4bd634ba4bf128a1930dfa97a0187")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-cli@2.5:", type=("build", "run"))
	depends_on("r-dplyr@1.0.6:", type=("build", "run"))
	depends_on("r-dtplyr@1.1:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-sunburstr", type=("build", "run"))
	depends_on("r-tibble@3.1.2:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
