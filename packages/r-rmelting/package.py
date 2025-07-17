# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmelting(RPackage):
    """R Interface to MELTING 5

    R interface to the MELTING 5 program (https://www.ebi.ac.uk/biomodels/tools/melting/) to compute melting temperatures of nucleic acid duplexes along with other thermodynamic parameters.
    """

    homepage = "https://github.com/aravind-j/rmelting"
    bioc = "rmelting"

    version("1.24.0", commit="f5bd86a1991f5e105f9aa82b6e22c27a29f77c0d")
    version("1.18.0", commit="0c3fef2e03ce06eace58359f04e23e1d89040e0d")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-rdpack", type=("build", "run"))
    depends_on("r-rjava@0.9.8:", type=("build", "run"))
    depends_on("openjdk", type=("build", "link", "run"))
