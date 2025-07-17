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

    version("1.30.0", commit="cfcf8668b2a9c871942b62b478244b0527e826bc")
    version("1.24.0", commit="e955a084143b9a157790a722a31029d269f49096")
