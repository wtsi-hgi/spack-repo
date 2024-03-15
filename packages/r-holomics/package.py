# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHolomics(RPackage):
	"""An User-Friendly R 'shiny' Application for Multi-Omics Data
Integration and Analysis

	A 'shiny' application, which allows you to perform single- and
    multi-omics analyses using your own omics datasets. After the upload 
    of the omics datasets and a metadata file, single-omics is performed
    for feature selection and dataset reduction. These datasets are used 
    for pairwise- and multi-omics analyses, where automatic tuning is 
    done to identify correlations between the datasets - the end goal 
    of the recommended 'Holomics' workflow.
    Methods used in the package were implemented in the package 'mixomics'
    by Florian Rohart,Benoît Gautier,Amrit Singh,Kim-Anh Lê Cao (2017) <doi:10.1371/journal.pcbi.1005752>
    and are described there in further detail.
	"""
	
	homepage = "https://github.com/MolinLab/Holomics"
	cran = "Holomics" 

	version("1.1.0", md5="dba4e884d9c214a9b9b4dc661e088003")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-bs4dash@2.0.2:", type=("build", "run"))
	depends_on("r-config", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-golem", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-shiny@1.6:", type=("build", "run"))
	depends_on("r-shinyalert", type=("build", "run"))
	depends_on("r-shinybusy", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinyvalidate", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tippy", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-mixomics", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
