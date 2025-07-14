# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCuratedatlasqueryr(RPackage):
	"""Queries the Human Cell Atlas

	Provides access to a copy of the Human Cell Atlas, but with harmonised metadata. This allows for uniform querying across numerous datasets within the Atlas using common fields such as cell type, tissue type, and patient ethnicity. Usage involves first querying the metadata table for cells of interest, and then downloading the corresponding cells into a SingleCellExperiment object.
	"""
	
	homepage = "https://github.com/stemangiola/CuratedAtlasQueryR"
	bioc = "CuratedAtlasQueryR"

	version("1.6.0", commit="38a4d0ae2565537a248791386b02cb405c11a797")
	version("1.0.1", commit="bb3acd7792a2f2e4427b644cc8281cdae00bacac")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-purrr@1:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-hdf5array", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-seuratobject", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dbplyr@2.3:", type=("build", "run"))
	depends_on("r-duckdb", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
