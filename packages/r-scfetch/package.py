# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScfetch(RPackage):
	"""Access and Format Single-Cell RNA-Seq Datasets from Public
Resources

	The goal of 'scfetch' is to access and format single-cell RNA-seq datasets. It can be used to download single-cell RNA-seq
    datasets from widely used public resources, including GEO <https://www.ncbi.nlm.nih.gov/geo/>, Zenodo <https://zenodo.org/>, 
    CELLxGENE <https://cellxgene.cziscience.com/>, Human Cell Atlas <https://www.humancellatlas.org/>, PanglaoDB <https://panglaodb.se/index.html> 
    and UCSC Cell Browser <https://cells.ucsc.edu/>. And, it can also be used to perform object conversion between SeuratObject <https://satijalab.org/seurat/>, 
    loom <http://loompy.org/>, h5ad <https://scanpy.readthedocs.io/en/stable/>, SingleCellExperiment <https://bioconductor.org/packages/release/bioc/html/scran.html>, 
    CellDataSet <http://cole-trapnell-lab.github.io/monocle-release/> and cell_data_set <https://cole-trapnell-lab.github.io/monocle3/>.
	"""
	
	homepage = "https://github.com/showteeth/scfetch"
	cran = "scfetch" 

	version("0.5.0", md5="547510a8df5c6a8e3c56d4bc6fae6472")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-geoquery", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rpanglaodb", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-scater", type=("build", "run"))
	depends_on("r-loomexperiment", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
