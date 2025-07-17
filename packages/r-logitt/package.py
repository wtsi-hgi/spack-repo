# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLogitt(RPackage):
    """logit-t Package

    The logitT library implements the Logit-t algorithm introduced in --A high performance test of differential gene expression for oligonucleotide arrays-- by William J Lemon, Sandya Liyanarachchi and Ming You for use with Affymetrix data stored in an AffyBatch object in R.
    """

    homepage = "http://www.bioconductor.org"
    bioc = "logitT"

    version("1.60.0", commit="bc447532e4373ec975804959770039cdcaa11ad3")

    depends_on("r-affy", type=("build", "run"))
