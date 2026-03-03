# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcal1(RPackage):
    """L1-Norm PCA Methods

    Implementations of several methods for principal component analysis
        using the L1 norm.  The package depends on COIN-OR Clp version >=
        1.17.4.  The methods implemented are
        PCA-L1 (Kwak 2008) <DOI:10.1109/TPAMI.2008.114>,
        L1-PCA (Ke and Kanade 2003, 2005) <DOI:10.1109/CVPR.2005.309>,
        L1-PCA* (Brooks, Dula, and Boone 2013) <DOI:10.1016/j.csda.2012.11.007>,
        L1-PCAhp (Visentin, Prestwich and Armagan 2016)
                 <DOI:10.1007/978-3-319-46227-1_37>,
        wPCA (Park and Klabjan 2016) <DOI: 10.1109/ICDM.2016.0054>,
        awPCA (Park and Klabjan 2016) <DOI: 10.1109/ICDM.2016.0054>,
        PCA-Lp (Kwak 2014) <DOI:10.1109/TCYB.2013.2262936>, and
        SharpEl1-PCA (Brooks and Dula, submitted).
    """

    cran = "pcaL1"

    version(
        "1.5.7", md5="3e92f99030a222ee3a6c93ca93d51c69", url="https://cran.r-project.org/src/contrib/pcaL1_1.5.7.tar.gz"
    )

    depends_on("clp")
