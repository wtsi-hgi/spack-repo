# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsbackendmsp(RPackage):
    """Mass Spectrometry Data Backend for NIST msp Files

    Mass spectrometry (MS) data backend supporting import and handling of MS/MS spectra from NIST MSP Format (msp) files. Import of data from files with different MSP *flavours* is supported. Objects from this package add support for MSP files to Bioconductor's Spectra package. This package is thus not supposed to be used without the Spectra package that provides a complete infrastructure for MS data handling.
    """

    homepage = "https://github.com/RforMassSpectrometry/MsBackendMsp"
    bioc = "MsBackendMsp"

    version("1.12.0", commit="5d6dc9b824ced524dce09a61c172508d5a329ac4")
    version("1.6.0", commit="08ab2178dd77a0e6d4a57232d5813ccf56869990")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-spectra@1.5.14:", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-mscoreutils", type=("build", "run"))
