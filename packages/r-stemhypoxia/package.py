# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStemhypoxia(RPackage):
    """Differentiation of Human Embryonic Stem Cells under Hypoxia gene expression dataset by Prado-Lopez et al. (2010)

    Expression profiling using microarray technology to prove if 'Hypoxia Promotes Efficient Differentiation of Human Embryonic Stem Cells to Functional Endothelium' by Prado-Lopez et al. (2010) Stem Cells 28:407-418. Full data available at Gene Expression Omnibus series GSE37761.
    """

    homepage = "http://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE37761"
    bioc = "stemHypoxia"

    version("1.44.0", commit="b95325d3d6d4298975011a2ff0403cd34140b550")
    version("1.38.0", commit="97a19070969bf3236dfd0c80de025533aa369769")

    depends_on("r@2.14.1:", type=("build", "run"))
