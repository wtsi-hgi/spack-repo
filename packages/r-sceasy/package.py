# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RSceasy(RPackage):
    """sceasy is a package that helps easy conversion of different single-cell data formats to each other. Converting to AnnData creates a file that can be directly used in cellxgene which is an interactive explorer for single-cell transcriptomics datasets."""

    homepage = "https://github.com/cellgeni/sceasy"
    url = "https://github.com/cellgeni/sceasy/archive/refs/tags/v0.0.7.tar.gz"

    version("0.0.7", sha256="bc6a2dba2111067f3247ff1ee617cc85ab6c7d89950f7d8ca486a3e34b27f9d6")
    version("0.0.6", sha256="4636160799ff39e22bcae65171c689140fdcbe3525330f1dc532892316ac23dd")
    version("0.0.5", sha256="70f028ab3e29384063d339ae5a596dd64692960f52b2ba073148a2ea2d484817")
    version("0.0.4", sha256="2b0e53152d8cf8ac93fd6446255d092d67795177be45fea74a6e6d9cf9fdf7a1")
    version("0.0.3", sha256="fed2cf92965e81297f8b556e5d119a366a84679101b78567a16d72416b4a72e6")
    version("0.0.2", sha256="fbf13f819202ab3c1d45e1582e1ee965038d80f35dc236e581c1373b5fc7ea97")
    version("0.0.1", sha256="6716146c26980aefc043dc97141087481d66374bc43991a124a7a99ede19549d")

    depends_on("r-reticulate", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
