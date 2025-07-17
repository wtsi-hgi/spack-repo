# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsygenet2r(RPackage):
    """psygenet2r - An R package for querying PsyGeNET and to perform comorbidity studies in psychiatric disorders

    Package to retrieve data from PsyGeNET database (www.psygenet.org) and to perform comorbidity studies with PsyGeNET's and user's data.
    """

    bioc = "psygenet2r"

    version("1.34.1", commit="1dce02c38d521200ad46bda8f8c5441c9e9f00f9")

    depends_on("r@3.4:", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-rcurl", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-biomart", type=("build", "run"))
    depends_on("r-bgeedb", type=("build", "run"))
    depends_on("r-topgo", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-labeling", type=("build", "run"))
    depends_on("r-go-db", type=("build", "run"))
