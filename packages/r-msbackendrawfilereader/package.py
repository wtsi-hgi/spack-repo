# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsbackendrawfilereader(RPackage):
    """Mass Spectrometry Backend for Reading Thermo Fisher Scientific raw Files

    implements a MsBackend for the Spectra package using Thermo Fisher Scientific's NewRawFileReader .Net libraries. The package is generalizing the functionality introduced by the rawrr package Methods defined in this package are supposed to extend the Spectra Bioconductor package.
    """

    homepage = "https://github.com/fgcz/MsBackendRawFileReader"
    bioc = "MsBackendRawFileReader"

    version("1.14.0", commit="a5e44a08d468aa95071ab8c10c3a646d97d1e22d")
    version("1.8.1", commit="3a566d9dfc622320e01ac613eb5934e23dd75e9a")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-spectra@1.5.8:", type=("build", "run"))
    depends_on("r-mscoreutils", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-rawrr@1.10.1:", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
