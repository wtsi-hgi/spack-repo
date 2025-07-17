# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNupop(RPackage):
    """An R package for nucleosome positioning prediction

    NuPoP is an R package for Nucleosome Positioning Prediction.This package is built upon a duration hidden Markov model proposed in Xi et al, 2010; Wang et al, 2008. The core of the package was written in Fotran. In addition to the R package, a stand-alone Fortran software tool is also available at https://github.com/jipingw. The Fortran codes have complete functonality as the R package.  Note: NuPoP has two separate functions for prediction of nucleosome positioning, one for MNase-map trained models and the other for chemical map-trained models. The latter was implemented for four species including yeast, S.pombe, mouse and human, trained based on our recent publications. We noticed there is another package nuCpos by another group for prediction of nucleosome positioning trained with chemicals. A report to compare recent versions of NuPoP with nuCpos can be found at https://github.com/jiping/NuPoP_doc. Some more information can be found and will be posted at https://github.com/jipingw/NuPoP.
    """

    bioc = "NuPoP"

    version("2.16.0", commit="d323be0dab4531a87652dc1ebfc562e9f562489d")
    version("2.10.0", commit="34970309ddaa40fc479cc412b90f918120f669dc")

    depends_on("r@4:", type=("build", "run"))
