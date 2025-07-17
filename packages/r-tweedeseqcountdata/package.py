# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTweedeseqcountdata(RPackage):
    """RNA-seq count data employed in the vignette of the tweeDEseq package

    RNA-seq count data from Pickrell et al. (2010) employed to illustrate the use of the Poisson-Tweedie family of distributions with the tweeDEseq package.
    """

    homepage = "https://github.com/isglobal-brge/tweeDEseqCountData/"
    bioc = "tweeDEseqCountData"

    version("1.46.0", commit="bf1977be57c34be5df134c571b8103bb36541476")
    version("1.40.0", commit="8fcf8beb5b15b728311b10bc6ea34161454a8df7")

    depends_on("r-biobase", type=("build", "run"))
    depends_on("r@4.3:", type=("build", "run"))
