# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRecountworkflow(RPackage):
	"""recount workflow: accessing over 70,000 human RNA-seq samples with Bioconductor

	The recount2 resource is composed of over 70,000 uniformly processed human RNA-seq samples spanning TCGA and SRA, including GTEx. The processed data can be accessed via the recount2 website and the recount Bioconductor package. This workflow explains in detail how to use the recount package and how to integrate it with other Bioconductor packages for several analyses that can be carried out with the recount2 resource. In particular, we describe how the coverage count matrices were computed in recount2 as well as different ways of obtaining public metadata, which can facilitate downstream analyses. Step-by-step directions show how to do a gene level differential expression analysis, visualize base-level genome coverage data, and perform an analyses at multiple feature levels. This workflow thus provides further information to understand the data in recount2 and a compendium of R code to use the data.
	"""
	
	homepage = "https://github.com/LieberInstitute/recountWorkflow"
	bioc = "recountWorkflow" 
	urls = ["https://www.bioconductor.org/packages/3.18/workflows/src/contrib/recountWorkflow_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/workflows/src/contrib/Archive/recountWorkflow/recountWorkflow_1.26.0.tar.gz"]

	version("1.32.0", tag="RELEASE_3_21")
	version("1.26.0", sha256="2a1546ad31685e789e0ad235b8ebc26524291bd112dc071883389b0330932799")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-recount", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-regionreport", type=("build", "run"))
	depends_on("r-clusterprofiler", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-derfinder", type=("build", "run"))
	depends_on("r-genomicstate", type=("build", "run"))
	depends_on("r-bumphunter", type=("build", "run"))
	depends_on("r-derfinderplot", type=("build", "run"))

