# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFortunes(RPackage):
    """R Fortunes
    
    A collection of fortunes from the R community.
    """

    cran = "fortunes"

    version("1.5-4", sha256="af55c5885336d989368410256a57a0e917cf4b3a486d4592f0d0587767f23481")

