# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsd16s(RPackage):
    """Healthy and moderate to severe diarrhea 16S expression data

    Gut 16S sequencing expression data from 992 healthy and moderate-to-severe diarrhetic samples used in 'Diarrhea in young children from low-income countries leads to large-scale alterations in intestinal microbiota composition'.
    """

    homepage = "http://www.cbcb.umd.edu/research/projects/GEMS-pathogen-discovery"
    bioc = "msd16s"

    version("1.28.0", commit="440836dea1234afb98d82c2116959ec6ae6ed3ef")
    version("1.22.0", commit="437172b0e2468c872888f1cb255e2efa39ae7d87")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-metagenomeseq", type=("build", "run"))
