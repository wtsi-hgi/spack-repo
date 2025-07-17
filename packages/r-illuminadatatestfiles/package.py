# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIlluminadatatestfiles(RPackage):
    """Illumina microarray files (IDAT) for testing

    Example data for Illumina microarray output files, for testing purposes
    """

    bioc = "IlluminaDataTestFiles"

    version("1.46.0", commit="66584047cddb5279525acde0d935235df0ba8bb7")
    version("1.40.0", commit="3aa73775367c60d6648a6c821177df44ba1889c3")
