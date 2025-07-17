# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHivcdnavantwout03(RPackage):
    """T cell line infections with HIV-1 LAI (BRU)

    The expression levels of approximately 4600 cellular RNA transcripts were assessed in CD4+ T cell lines at different times after infection with HIV-1BRU using DNA microarrays. This data corresponds to the first block of a 12 block array image (001030_08_1.GEL) in the first data set (2000095918 A) in the first experiment (CEM LAI vs HI-LAI 24hr). There are two data sets, which are part of a dye-swap experiment with replicates, representing the Cy3 (green) absorption intensities for channel 1 (hiv1raw) and the Cy5 (red) absorption intensities for channel 2 (hiv2raw).
    """

    homepage = (
        "http://expression.microslu.washington.edu/expression/vantwoutjvi2002.html"
    )
    bioc = "HIVcDNAvantWout03"

    version("1.48.0", commit="d317f0a7a4d93ccc2c04802800d80e018eadf862")
    version("1.42.0", commit="f5b3146d82fba742a8d9bc2f27c7ee0625b5a70f")
