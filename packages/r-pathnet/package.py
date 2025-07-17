# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPathnet(RPackage):
    """An R package for pathway analysis using topological information

    PathNet uses topological information present in pathways and differential expression levels of genes (obtained from microarray experiment) to identify pathways that are 1) significantly enriched and 2) associated with each other in the context of differential expression. The algorithm is described in: PathNet: A tool for pathway analysis using topological information. Dutta B, Wallqvist A, and Reifman J. Source Code for Biology and Medicine 2012 Sep 24;7(1):10.
    """

    bioc = "PathNet"

    version("1.48.0", commit="772b0c230a6395cc052d8904dcdb7295b804d09b")
    version("1.42.0", commit="f524fe672e9ab71f0c0e0228cfb3e7e5ac6af9d5")
