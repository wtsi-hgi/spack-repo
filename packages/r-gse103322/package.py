# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGse103322(RPackage):
	"""GEO accession data GSE103322 as a SingleCellExperiment

	Single cell RNA-Seq data for 5902 cells from 18 patients with oral cavity head and neck squamous cell carcinoma available as GEO accession [GSE103322] (http://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE103322). GSE103322 data have been parsed into a SincleCellExperiment object available in ExperimentHub.
	"""
	
	bioc = "GSE103322"

	version("1.14.0", commit="9f32c394859b43152e2ed503cb426f3c15a53870")
	version("1.8.0", commit="ca9003d9e8ba3bc257e344effae25b6641e7a22a")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-geoquery", type=("build", "run"))

