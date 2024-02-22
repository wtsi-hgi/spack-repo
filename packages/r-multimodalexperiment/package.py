# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultimodalexperiment(RPackage):
	"""Integrative Bulk and Single-Cell Experiment Container

	MultimodalExperiment is an S4 class that integrates bulk and single-cell experiment data; it is optimally storage-efficient, and its methods are exceptionally fast. It effortlessly represents multimodal data of any nature and features normalized experiment, subject, sample, and cell annotations, which are related to underlying biological experiments through maps. Its coordination methods are opt-in and employ database-like join operations internally to deliver fast and flexible management of multimodal data.
	"""
	
	bioc = "MultimodalExperiment" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/MultimodalExperiment_1.2.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/MultimodalExperiment/MultimodalExperiment_1.2.0.tar.gz"]

	version("1.2.0", md5="376186ba5972df1b6d4be9dc69253a61")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
