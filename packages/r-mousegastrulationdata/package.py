# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMousegastrulationdata(RPackage):
	"""Single-Cell -omics Data across Mouse Gastrulation and Early Organogenesis

	Provides processed and raw count data for single-cell RNA sequencing, single-cell ATAC-seq, and seqFISH (spatial transcriptomic) experiments performed along a timecourse of mouse gastrulation and early organogenesis.
	"""
	
	homepage = "https://github.com/MarioniLab/MouseGastrulationData"
	bioc = "MouseGastrulationData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/MouseGastrulationData_1.16.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/MouseGastrulationData/MouseGastrulationData_1.16.0.tar.gz"]

    version("1.22.0", tag="RELEASE_3_21")
	version("1.16.0", sha256="20369acb93d3ae208773d6394888d95930f6d24292495933609e42f770e60354")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-spatialexperiment", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-bumpymatrix", type=("build", "run"))

