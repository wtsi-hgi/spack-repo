# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiocmetaworkflow(RPackage):
	"""BioC Workflow about publishing a Bioc Workflow

	Bioconductor Workflow describing how to use BiocWorkflowTools to work with a single R Markdown document to submit to both Bioconductor and F1000Research.
	"""
	
	bioc = "BiocMetaWorkflow" 
	urls = ["https://www.bioconductor.org/packages/3.18/workflows/src/contrib/BiocMetaWorkflow_1.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/workflows/src/contrib/Archive/BiocMetaWorkflow/BiocMetaWorkflow_1.24.0.tar.gz"]

    version("1.30.0", tag="RELEASE_3_21")
	version("1.24.0", sha256="10ba2ef2402780213da6ba8b6f84128b04e1f39a5b33e10da963113ea0bdd319")


