# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpeckle(RPackage):
	"""Statistical methods for analysing single cell RNA-seq data

	The speckle package contains functions for the analysis of single cell RNA-seq data. The speckle package currently contains functions to analyse differences in cell type proportions. There are also functions to estimate the parameters of the Beta distribution based on a given counts matrix, and a function to normalise a counts matrix to the median library size. There are plotting functions to visualise cell type proportions and the mean-variance relationship in cell type proportions and counts. As our research into specialised analyses of single cell data continues we anticipate that the package will be updated with new functions.
	"""
	
	bioc = "speckle"

	version("1.8.0", commit="8b8d884e63c575d96d8ee95ce542a85248ec5c0f")
	version("1.2.0", commit="fde77d22a2568dcd1086d9265ed521b9946635da")
	version("0.0.3", git="https://github.com/Oshlack/speckle.git", commit="9347bf07b5cdc49ecedc0042d3a007742db01691")

	depends_on("r@4.2:", type=("build", "run"), when="@1.2.0:")
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"), when="@0.0.3")
	depends_on("r-caret", type=("build", "run"), when="@0.0.3")
	depends_on("r-scuttle", type=("build", "run"), when="@0.0.3")
	depends_on("r-stringr", type=("build", "run"), when="@0.0.3")
	depends_on("r-annotationdbi", type=("build", "run"), when="@0.0.3")
	depends_on("r-org-hs-eg-db", type=("build", "run"), when="@0.0.3")
	depends_on("r-org-mm-eg-db", type=("build", "run"), when="@0.0.3")
